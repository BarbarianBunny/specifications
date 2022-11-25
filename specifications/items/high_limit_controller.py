from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class HighLimitController(Item):
    item_group = ItemGroup.equipment

    kp_34_060_2148 = None
    kp_36_060_217891 = None
    l404c1147 = None
    l404c1162 = None
    l4079b1033 = None
    l4079b1041 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, range_min: int, range_max: int,
                 range_unit: Unit = Unit.pounds_per_square_inch, honeywell_upgrade=None, manual: str or None = None,
                 datasheet: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.range = Spec("Range", f"{range_min} - {range_max}", range_unit)
        self.honeywell_upgrade = honeywell_upgrade

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

    @item_property
    def honeywell_upgrade(self):
        return self._honeywell_upgrade

    @honeywell_upgrade.setter
    def honeywell_upgrade(self, item):
        self._honeywell_upgrade = Spec("Honeywell Upgrade", item)

    def __str__(self):
        return f"{self.model}"


# Danfoss
HighLimitController.kp_34_060_2148 = HighLimitController(Make.danfoss, "KP34 060-2148", 2, 15,
                                                         Unit.pounds_per_square_inch, None, "Danfoss KP manual.pdf",
                                                         "Danfoss KP KPI datasheet.pdf")
HighLimitController.kp_36_060_217891 = HighLimitController(Make.danfoss, "KP36 060-217891", 15, 150,
                                                           Unit.pounds_per_square_inch, None, "Danfoss KP manual.pdf",
                                                           "Danfoss KP KPI datasheet.pdf")

# Honeywell
HighLimitController.l404c1147 = HighLimitController(Make.honeywell, "L404C1147", 0, 15,
                                                    Unit.pounds_per_square_inch, None, "Honeywell L404x L604x manual.pdf")
HighLimitController.l404c1162 = HighLimitController(Make.honeywell, "L404C1162", 10, 150,
                                                    Unit.pounds_per_square_inch, None, "Honeywell L404x L604x manual.pdf")
HighLimitController.l4079b1033 = HighLimitController(Make.honeywell, "L4079B1033", 2, 15,
                                                     Unit.pounds_per_square_inch, None, "Honeywell L4079xxxxx manual.pdf")
HighLimitController.l4079b1041 = HighLimitController(Make.honeywell, "L4079B1041", 10, 150,
                                                     Unit.pounds_per_square_inch, None, "Honeywell L4079xxxxx manual.pdf")

# Honeywell Upgrade
HighLimitController.kp_34_060_2148.honeywell_upgrade = HighLimitController.l4079b1033
HighLimitController.kp_36_060_217891.honeywell_upgrade = HighLimitController.l4079b1041
HighLimitController.l404c1147.honeywell_upgrade = HighLimitController.l4079b1033
HighLimitController.l404c1162.honeywell_upgrade = HighLimitController.l4079b1041


# for var in vars(HighLimitController):
#     print(var)
