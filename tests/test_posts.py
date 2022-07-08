import pytest
import requests
from assertpy.assertpy import assert_that

import core.helpers
from core.helpers import validate

from core import data

post_schema = "core/files/post_schema.json"


class TestBaseActions:

    def test_get_posts_list(self, get_posts_list):
        assert_that(get_posts_list.status_code).is_equal_to(requests.codes.ok)
        assert_that(get_posts_list.body).is_not_empty()

        for post in get_posts_list.body:
            validate(post_schema, post)

    @pytest.mark.parametrize('get_post', [1], indirect=True)
    def test_get_post(self, get_post: core.helpers.Response):
        assert_that(get_post.status_code).is_equal_to(requests.codes.ok)

        validate(post_schema, get_post.body)

    @pytest.mark.parametrize('create_post',
                             [core.data.CreatePost.body],
                             indirect=True)
    def test_create_post(self, create_post: core.helpers.Response):
        """Regarding documentation: resource will not be really updated on the
         server, but it will be faked as if."""

        assert_that(create_post.status_code).is_equal_to(requests.codes.created)
        assert_that(create_post.body["body"]).is_equal_to("bar1")
        assert_that(create_post.body["userId"]).is_equal_to(1)

        validate(post_schema, create_post.body)

    @pytest.mark.parametrize('update_post',
                             [(core.data.UpdatePost.post_id,
                               core.data.UpdatePost.body)],
                             indirect=True)
    def test_update_post(self, update_post: core.helpers.Response):
        """Regarding documentation: resource will not be really updated on the
         server, but it will be faked as if."""

        assert_that(update_post.status_code).is_equal_to(requests.codes.ok)
        assert_that(update_post.body["body"]).is_equal_to("bar2")
        assert_that(update_post.body["userId"]).is_equal_to(1)

        validate(post_schema, update_post.body)

    @pytest.mark.parametrize('patch_post',
                             [(core.data.PatchPost.post_id,
                               core.data.PatchPost.body)],
                             indirect=True)
    def test_patch_post(self, patch_post: core.helpers.Response):
        """Regarding documentation: resource will not be really updated on the
         server, but it will be faked as if."""

        assert_that(patch_post.status_code, requests.codes.ok)
        assert_that(patch_post.body["title"]).is_equal_to("foo123")
        assert_that(patch_post.body["userId"]).is_equal_to(1)
        validate(post_schema, patch_post.body)

    @pytest.mark.parametrize('delete_post', [1], indirect=True)
    def test_delete_post(self, delete_post: core.helpers.Response):
        """Regarding documentation: resource will not be really updated on the
         server, but it will be faked as if."""

        assert_that(delete_post.status_code).is_equal_to(requests.codes.ok)
