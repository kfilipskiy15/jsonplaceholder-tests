import requests


def get_posts_list(URL):
    response = requests.get(URL)
    return response


def get_post(URL, post_id):
    response = requests.get(f'{URL}{post_id}')
    return response


def create_post(URL, json):
    response = requests.post(URL, json=json)
    return response


def put_post(URL, user_id, json):
    response = requests.put(f'{URL}{user_id}', json=json)
    return response


def path_post(URL, user_id, json):
    response = requests.patch(f'{URL}{user_id}', json=json)
    return response


def delete_post(URL, post_id):
    response = requests.delete(f'{URL}{post_id}')
    return response
