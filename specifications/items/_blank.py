from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Blank(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"

# for var in vars(Blank):
#     print(var)
