import re

from yaml import load, FullLoader

from collections.abc import Mapping


class Content(Mapping):

    __delimeter = "^(?:-/\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self):
        _ = __regex.split('', 2)
        fm = __regex.split('', 2)
        content = __regex.split('', 2)
