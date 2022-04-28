# from asyncio import as_completed
# from modulefinder import packagePathMap
# import pstats
import requests
from assertpy.assertpy import assert_that

URL = "https://jsonplaceholder.typicode.com/posts/"


def test_get_posts_list():
    re = requests.get(URL)
    posts_list = re.json()

    assert_that(re.status_code).is_equal_to(requests.codes.ok)
    assert_that(posts_list).is_not_empty()
    for post in posts_list:
        assert_that(post).contains_key("userId")
        assert_that(post).contains_key("id")
        assert_that(post).contains_key("title")
        assert_that(post).contains_key("body")


def test_get_post():
    re = requests.get(f'{URL}1')
    post_object = re.json()

    assert_that(re.status_code).is_equal_to(requests.codes.ok)
    assert_that(post_object).contains_key("userId")
    assert_that(post_object).contains_key("id")
    assert_that(post_object).contains_key("title")
    assert_that(post_object).contains_key("body")


def test_create_post():
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""
    json = {
        "title": "foo",
        "body": "bar1",
        "userId": 1
    }
    resp = requests.post(URL, json=json)
    post_object = resp.json()

    assert_that(resp.status_code).is_equal_to(requests.codes.created)
    assert_that(post_object).contains_key("id")
    assert_that(post_object).contains("title").contains_value("foo")
    assert_that(post_object).contains("body").contains_value("bar1")
    assert_that(post_object).contains("userId").contains_value(1)


def test_update_post():
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    json = {
        "id": 1,
        "title": "foo",
        "body": "bar2",
        "userId": 1
    }
    resp = requests.put(f'{URL}1', json=json)
    post_object = resp.json()

    assert_that(resp.status_code).is_equal_to(requests.codes.ok)
    assert_that(post_object).contains_key("id")
    assert_that(post_object).contains("title").contains_value("foo")
    assert_that(post_object).contains("body").contains_value("bar2")
    assert_that(post_object).contains("userId").contains_value(1)


def test_patch_post():
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    payload = {
        "title": "foo123"
    }
    resp = requests.patch(f'{URL}1', json=payload)
    post_object = resp.json()

    assert_that(resp.status_code).is_equal_to(requests.codes.ok)
    assert_that(post_object).contains_key("id")
    assert_that(post_object).contains_key("body")
    assert_that(post_object).contains("title").contains_value("foo123")
    assert_that(post_object).contains("userId").contains_value(1)


def test_delete_post():
    """Regarding documentation: resource will not be really updated on the server but it will be faked as if."""
    re = requests.delete(f'{URL}1')
    assert_that(re.status_code).is_equal_to(requests.codes.ok)
