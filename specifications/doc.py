import re


class Doc:
    def __init__(self, filename: str):
        self.filename = filename

    def __eq__(self, other):
        return self.filename == other.filename

    def __hash__(self):
        return hash(self.filename)

    def __lt__(self, other):
        return self.filename < other.filename

    def extension(self):
        return self.filename.split(".")[-1]

    def href(self):
        filename = re.sub(r",", "%2C", self.filename)
        filename = re.sub(r" ", "%20", filename)
        filename = re.sub(r"#", "%23", filename)
        return filename

    def title(self):
        return re.search(r"(.*)\.", self.filename).group(1)
