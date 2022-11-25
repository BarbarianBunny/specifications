from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.tank_type import TankType
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class FuelTank(Item):
    item_group = ItemGroup.equipment

    ul_142_double_wall_300 = None
    ul_142_double_wall_550 = None
    ul_142_double_wall_1100 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, tank_type: TankType, capacity, length: int or None,
                 diameter: int or None, weight: int, brochure: str or None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.type = Spec("Type", tank_type)
        self.capacity = Spec("Capacity", capacity, Unit.gallon)
        self.length = Spec("Length", length, Unit.inch)
        self.diameter = Spec("Diameter", diameter, Unit.inch)
        self.weight = Spec("Weight", weight, Unit.pounds)

        if brochure:
            self.doc_header = Spec(None, Header("Docs"))
        self.brochure = Spec("Brochure", Doc(brochure))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model} - {self.capacity}"


FuelTank.ul_142_double_wall_300 = FuelTank(Make.acetank, "UL-142 Double Wall", TankType.aboveground_storage_tank, 300,
                                           75, 39, 1000, "Acetank UL142 Double Wall Skid brochure.pdf")
FuelTank.ul_142_double_wall_550 = FuelTank(Make.acetank, "UL-142 Double Wall", TankType.aboveground_storage_tank, 550,
                                           75, 51, 1400, "Acetank UL142 Double Wall Skid brochure.pdf")
FuelTank.ul_142_double_wall_1100 = FuelTank(Make.acetank, "UL-142 Double Wall", TankType.aboveground_storage_tank, 1100,
                                            148, 51, 2400, "Acetank UL142 Double Wall Skid brochure.pdf")

# for var in vars(Blank):
#     print(var)
