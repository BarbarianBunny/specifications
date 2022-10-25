from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.spec import Spec


class Blank(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, blank):
        super().__init__()
        self.blank = Spec("Blank", blank)

    def __str__(self):
        return f"{self.blank}"
