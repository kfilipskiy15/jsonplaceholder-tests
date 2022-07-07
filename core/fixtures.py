from dataclasses import dataclass

import requests
from pytest import fixture

from core.helpers import get_response


@fixture
def get_posts_list(base_url) -> dataclass():
    r = requests.get(url=base_url)
    return get_response(r)


@fixture(scope="function")
def get_post(base_url, request) -> dataclass():
    r = requests.get(url=base_url + str(request.param))
    return get_response(r)


@fixture(scope="function")
def create_post(base_url, request) -> dataclass():
    r = requests.post(url=base_url, json=request.param)
    return get_response(r)


@fixture(scope="function")
def update_post(base_url, request) -> dataclass():
    r = requests.put(url=base_url + str(request.param[0]),
                     json=request.param[1])
    return get_response(r)


@fixture(scope="function")
def patch_post(base_url, request) -> dataclass():
    r = requests.patch(url=base_url + str(request.param[0]),
                       json=request.param[1])
    return get_response(r)


@fixture(scope="function")
def delete_post(base_url, request) -> dataclass():
    r = requests.delete(url=base_url + str(request.param))
    return get_response(r)
