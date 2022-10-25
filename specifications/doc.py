import re

from specifications.support_modules.convert_case import ConvertCase


class Doc:
    def __init__(self, filename: str):
        self.filename = filename

    def __lt__(self, other):
        return self.filename < other.filename

    def extension(self):
        return self.filename.split(".")[-1]

    def href(self):
        filename = re.sub(r",", "%2C", self.filename)
        filename = re.sub(r" ", "%20", filename)
        return filename

    def name(self):
        return re.search(r"(.*)\.", self.filename).group(1)

    def title(self):
        return ConvertCase.remove_kebab(self.name())
