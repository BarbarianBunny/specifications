from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.spec import Spec


class Fuse(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, fuse_model, amperage):
        super().__init__()
        self.fuse_model = Spec("Model", fuse_model)
        self.amperage = Spec("Amperage", amperage, Unit.amp)

    def __str__(self):
        return f"{self.fuse_model} {self.amperage}"
