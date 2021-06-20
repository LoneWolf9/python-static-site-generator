import re

from yaml import load, FullLoader

from collections.abc import Mapping


class Content(Mapping):

    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        data = metadata
        self.data = {
            "content": content
        }

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    def set_type(self, x):
        self.data["type"] = x

    def
