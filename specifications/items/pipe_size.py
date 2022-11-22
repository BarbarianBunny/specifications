from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class PipeSize(Item):
    item_group = ItemGroup.specs

    d0_0625 = None
    d0_125 = None
    d0_25 = None
    d0_375 = None
    d0_5 = None
    d0_75 = None
    d1 = None
    d1_25 = None
    d1_5 = None
    d2 = None
    d2_5 = None
    d3 = None
    d3_5 = None
    d4 = None
    d4_5 = None
    d5 = None
    d6 = None
    d8 = None
    d10 = None
    d12 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, decimal: int or float, fraction: str or int, npt_outside_diameter: float,
                 npt_thread_per_inch: int or str):
        super().__init__()
        self.decimal = Spec("Decimal", decimal, Unit.inch)
        self.fraction = Spec("Fraction", fraction, Unit.inch)
        self.npt_outside_diameter = Spec("NPT OD", npt_outside_diameter, Unit.inch)
        self.npt_thread_per_inch = Spec("NPT TPI", npt_thread_per_inch)

    def __str__(self):
        return f"{self.decimal}"


PipeSize.d0_0625 = PipeSize(.0625, "1/16", .313, 27)
PipeSize.d0_125 = PipeSize(.125, "1/8", .405, 27)
PipeSize.d0_25 = PipeSize(.25, "1/4", .54, 18)
PipeSize.d0_375 = PipeSize(.375, "3/8", .675, 18)
PipeSize.d0_5 = PipeSize(.5, "1/2", .84, 14)
PipeSize.d0_75 = PipeSize(.75, "3/4", 1.05, 14)
PipeSize.d1 = PipeSize(1, "1", 1.315, "11-1/2")
PipeSize.d1_25 = PipeSize(1.25, "1-1/4", 1.66, "11-1/2")
PipeSize.d1_5 = PipeSize(1.5, "1-1/2", 1.9, "11-1/2")
PipeSize.d2 = PipeSize(2, "2", 2.375, "11-1/2")
PipeSize.d2_5 = PipeSize(2.5, "2-1/2", 2.875, 8)
PipeSize.d3 = PipeSize(3, "3", 3.5, 8)
PipeSize.d3_5 = PipeSize(3.5, "3-1/2", 4, 8)
PipeSize.d4 = PipeSize(4, "4", 4.5, 8)
PipeSize.d4_5 = PipeSize(4.5, "4-1/2", 5, 8)
PipeSize.d5 = PipeSize(5, "5", 5.563, 8)
PipeSize.d6 = PipeSize(6, "6", 6.625, 8)
PipeSize.d8 = PipeSize(8, "8", 8.625, 8)

# for var in vars(Blank):
#     print(var)
