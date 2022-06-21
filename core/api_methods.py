from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    headers: str
    body: object


def get_posts_list(URL):
    response = requests.get(URL)
    return get_response(response)


def get_post(URL, post_id):
    response = requests.get(f'{URL}{post_id}')
    return get_response(response)


def create_post(URL, json):
    response = requests.post(URL, json=json)
    return get_response(response)


def put_post(URL, user_id, json):
    response = requests.put(f'{URL}{user_id}', json=json)
    return get_response(response)


def path_post(URL, user_id, json):
    response = requests.patch(f'{URL}{user_id}', json=json)
    return get_response(response)


def delete_post(URL, post_id):
    response = requests.delete(f'{URL}{post_id}')
    return get_response(response)


def get_response(response):
    status_code = response.status_code
    headers = response.headers

    try:
        body = response.json()
    except Exception:
        body = {}

    return Response(status_code, headers, body)
