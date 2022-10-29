from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Blank(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, blank, blank2):
        super().__init__()
        self.blank = Spec("Blank", blank)
        self.blank2 = blank2

    @item_property
    def blank2(self):
        return self._blank2

    @blank2.setter
    def blank2(self, item):
        self._blank2 = Spec("Blank2", item)

    def __str__(self):
        return f"{self.blank}"
