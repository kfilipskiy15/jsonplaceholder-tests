import requests
from assertpy.assertpy import assert_that

from core.helpers import validate

post_schema = "core/files/post_schema.json"


def test_get_posts_list(posts_list):
    assert_that(posts_list.status_code).is_equal_to(requests.codes.ok)
    assert_that(posts_list.json()).is_not_empty()

    for post in posts_list.json():
        validate(post_schema, post)


def test_get_post(post):
    assert_that(post.status_code).is_equal_to(requests.codes.ok)

    validate(post_schema, post.json())


def test_create_post(new_post):
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    assert_that(new_post.status_code).is_equal_to(requests.codes.created)
    assert_that(new_post.json()).contains("body").contains_value("bar1")
    assert_that(new_post.json()).contains("userId").contains_value(1)

    validate(post_schema, new_post.json())


def test_update_post(updated_post):
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    assert_that(updated_post.status_code).is_equal_to(requests.codes.ok)
    assert_that(updated_post.json()).contains("body").contains_value("bar2")
    assert_that(updated_post.json()).contains("userId").contains_value(1)

    validate(post_schema, updated_post.json())


def test_patch_post(patched_post):
    """Regarding documentation: resource will not be really updated on the server
    but it will be faked as if."""

    assert_that(patched_post.status_code).is_equal_to(requests.codes.ok)
    assert_that(patched_post.json()).contains("title").contains_value("foo123")
    assert_that(patched_post.json()).contains("userId").contains_value(1)

    validate(post_schema, patched_post.json())


def test_delete_post(deleted_post):
    """Regarding documentation: resource will not be really updated on the server but it will be faked as if."""
    assert_that(deleted_post.status_code).is_equal_to(requests.codes.ok)


# def validate(json_schema, responce_body):
#     validator = Validator(read_json_file(json_schema), require_all=True)

#     assert validator.validate(responce_body) is True, validator.errors


# def read_json_file(file):
#     with open(file) as data:
#         json_object = json.load(data)
#     return json_object
