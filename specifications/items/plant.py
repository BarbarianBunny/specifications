from specifications.item import Item
from specifications.spec import Spec


class Plant(Item):
    def __init__(self, building):
        super().__init__()
        self.building = Spec("Building", building)