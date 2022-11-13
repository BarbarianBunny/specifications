import re

from specifications.support_modules.convert_case import ConvertCase


class Link:
    def __init__(self, url: str):
        self.url = url

    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)

    def __lt__(self, other):
        return self.url < other.url
