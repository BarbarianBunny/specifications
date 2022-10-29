from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.items.fuse_model import FuseModel
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Fuse(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, fuse_model, amperage):
        super().__init__()
        self.fuse_model = fuse_model
        self.amperage = Spec("Amperage", amperage, Unit.amp)

    @item_property
    def fuse_model(self):
        return self._fuse_model

    @fuse_model.setter
    def fuse_model(self, item):
        self._fuse_model = Spec("Model", item)

    def __str__(self):
        return f"{self.fuse_model} {self.amperage}"


Fuse.fnq_5_6 = Fuse(FuseModel.fnq, 5.6)
Fuse.fnq_r_3_5 = Fuse(FuseModel.fnq_r, 3.5)
Fuse.fnq_r_4 = Fuse(FuseModel.fnq_r, 4)