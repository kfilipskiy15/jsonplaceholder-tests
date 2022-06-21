import requests
from assertpy.assertpy import assert_that

from core.helpers import validate

post_schema = "core/files/post_schema.json"


def test_get_posts_list(posts_list):

    assert_that(posts_list.status_code).is_equal_to(requests.codes.ok)
    assert_that(posts_list.body).is_not_empty()
    for post in posts_list.body:
        validate(post_schema, post)


def test_get_post(post):
    assert_that(post.status_code).is_equal_to(requests.codes.ok)

    validate(post_schema, post.body)


def test_create_post(new_post):
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    assert_that(new_post.status_code).is_equal_to(requests.codes.created)
    assert_that(new_post.body["body"]).is_equal_to("bar1")
    assert_that(new_post.body["userId"]).is_equal_to(1)

    validate(post_schema, new_post.body)


def test_update_post(updated_post):
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    assert_that(updated_post.status_code).is_equal_to(requests.codes.ok)
    assert_that(updated_post.body["body"]).is_equal_to("bar2")
    assert_that(updated_post.body["userId"]).is_equal_to(1)

    validate(post_schema, updated_post.body)


def test_patch_post(patched_post):
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    assert_that(patched_post.status_code).is_equal_to(requests.codes.ok)
    assert_that(patched_post.body["title"]).is_equal_to("foo123")
    assert_that(patched_post.body["userId"]).is_equal_to(1)

    validate(post_schema, patched_post.body)


def test_delete_post(deleted_post):
    """Regarding documentation: resource will not be really updated on the server but it will be faked as if."""
    assert_that(deleted_post.status_code).is_equal_to(requests.codes.ok)
