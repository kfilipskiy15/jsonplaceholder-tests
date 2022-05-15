from pytest import fixture

import core.api_methods as api_methods
import config

URL = config.URL


@fixture(scope="function")
def posts_list():
    yield api_methods.get_posts_list(URL)


@fixture(scope="function")
def post():
    user_id = 1
    yield api_methods.get_post(URL, user_id)


@fixture(scope="function")
def new_post():
    payload = {
        "title": "foo",
        "body": "bar1",
        "userId": 1
    }
    yield api_methods.create_post(URL, json=payload)


@fixture(scope="function")
def updated_post():
    user_id = 1
    payload = {
        "id": 1,
        "title": "foo",
        "body": "bar2",
        "userId": 1
    }
    yield api_methods.put_post(URL, user_id, json=payload)


@fixture(scope="function")
def patched_post():
    user_id = 1
    payload = {
        "title": "foo123"
    }
    yield api_methods.path_post(URL, user_id, json=payload)


@fixture(scope="function")
def deleted_post():
    post_id = 1
    yield api_methods.delete_post(URL, post_id)
