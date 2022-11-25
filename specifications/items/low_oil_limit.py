from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class LowOilLimit(Item):
    item_group = ItemGroup.equipment

    b424v_xg6 = None
    kp36 = None
    l404v1061 = None
    l404v1087 = None
    daf_7081_153_9_k = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, part_number: str or int or None, range_min: int, range_max: int,
                 range_unit: Unit, diff_min: int or None, diff_max: int or None, diff_unit: Unit or None,
                 manual: str or None = None, datasheet: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.part_number = Spec("Part Number", part_number)
        self.range = Spec("Range", f"{range_min} - {range_max}", range_unit)
        self.diff = [diff_min, diff_max, diff_unit]

        if manual or datasheet:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.datasheet = Spec("Datasheet", Doc(datasheet))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    @property
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, items):
        if items[0] and items[1] and items[2]:
            self._diff = Spec("Diff", f"{items[0]} - {items[1]}", items[2])
        else:
            self._diff = Spec("Diff", None)

    def __str__(self):
        if self.part_number.value:
            return f"{self.model} - {self.part_number}"
        else:
            return f"{self.model}"


LowOilLimit.b424v_xg6 = LowOilLimit(Make.ashcroft, "B424V XG6", None, 0, 400, Unit.pounds_per_square_inch,
                                    None, None, None, None, "Ashcroft B Series Switches datasheet.pdf")
LowOilLimit.kp36 = LowOilLimit(Make.danfoss, "KP36", "0130602144", 15, 150, Unit.pounds_per_square_inch,
                               10, 55, Unit.pounds_per_square_inch, "Danfoss KP manual.pdf")
LowOilLimit.l404v1061 = LowOilLimit(Make.honeywell, "L404V1061", None, 25, 150, Unit.pounds_per_square_inch,
                                    8, 16, Unit.pounds_per_square_inch, "Honeywell L404 TVWY manual.pdf")
LowOilLimit.l404v1087 = LowOilLimit(Make.honeywell, "L404V1087", None, 10, 150, Unit.pounds_per_square_inch,
                                    10, 22, Unit.pounds_per_square_inch, "Honeywell L404 TVWY manual.pdf")
LowOilLimit.daf_7081_153_9_k = LowOilLimit(Make.ashcroft, "DAF-7081-153-9K", None, 10, 300, Unit.pounds_per_square_inch,
                                           None, None, None, "Mercoid D manual.pdf")

# for var in vars(LowOilLimit):
#     print(var)
