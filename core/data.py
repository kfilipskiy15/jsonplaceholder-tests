from dataclasses import dataclass

import core.helpers


@dataclass
class CreatePost:
    body = {
        "title": "foo",
        "body": "bar1",
        "userId": 1
    }


@dataclass
class UpdatePost:
    post_id = 2
    body = {
        "title": "foo",
        "body": "bar2",
        "userId": 1
    }


@dataclass
class PatchPost:
    post_id = 2
    body = {
        "title": "foo123"
    }
