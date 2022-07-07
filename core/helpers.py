import json
from dataclasses import dataclass

from cerberus import Validator


def validate(json_schema, response_body):
    validator = Validator(read_json_file(json_schema), require_all=True)

    assert validator.validate(response_body) is True, validator.errors
    return validator


def read_json_file(file_path: str):
    with open(file_path) as data:
        json_object = json.load(data)
    return json_object


@dataclass
class Response:
    status_code: int
    headers: str
    body: dict


def get_response(response):
    status_code = response.status_code
    headers = response.headers

    try:
        body = response.json()
    except Exception:
        body = {}

    return Response(status_code, headers, body)
