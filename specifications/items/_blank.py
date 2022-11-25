from specifications.doc import Doc
from specifications.header import Header
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Blank(Item):
    item_group = ItemGroup.equipment

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str,
                 manual: str or None = None, datasheet: str or None = None,
                 parts_list: str or None = None, catalogue: str or None = None, ):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)

        if manual or datasheet or parts_list or catalogue:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.datasheet = Spec("Datasheet", Doc(datasheet))
        self.parts_list = Spec("Parts List", Doc(parts_list))
        self.catalogue = Spec("Catalogue", Doc(catalogue))

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
