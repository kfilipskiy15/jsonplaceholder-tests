import pytest
from pytest import fixture

import core.api_methods as api_methods


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action = "store",
        default = "https://jsonplaceholder.typicode.com/posts/",
    )

@fixture(scope="session", autouse=True)
def base_url(request):
    return request.config.getoption("--url")

@fixture(scope="function")
def posts_list(base_url):
    yield api_methods.get_posts_list(base_url)


@fixture(scope="function")
def post(base_url):
    user_id = 1
    yield api_methods.get_post(base_url, user_id)


@fixture(scope="function")
def new_post(base_url):
    payload = {
        "title": "foo",
        "body": "bar1",
        "userId": 1
    }
    yield api_methods.create_post(base_url, json=payload)


@fixture(scope="function")
def updated_post(base_url):
    user_id = 1
    payload = {
        "id": 1,
        "title": "foo",
        "body": "bar2",
        "userId": 1
    }
    yield api_methods.put_post(base_url, user_id, json=payload)


@fixture(scope="function")
def patched_post(base_url):
    user_id = 1
    payload = {
        "title": "foo123"
    }
    yield api_methods.path_post(base_url, user_id, json=payload)


@fixture(scope="function")
def deleted_post(base_url):
    post_id = 1
    yield api_methods.delete_post(base_url, post_id)
