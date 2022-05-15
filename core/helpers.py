import json

from cerberus import Validator


def validate(json_schema, responce_body):
    validator = Validator(read_json_file(json_schema), require_all=True)

    assert validator.validate(responce_body) is True, validator.errors
    return validator


def read_json_file(file):
    with open(file) as data:
        json_object = json.load(data)
    return json_object
