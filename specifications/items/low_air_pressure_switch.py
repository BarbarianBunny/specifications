from specifications.enums.item_group import ItemGroup
from specifications.header import Header
from specifications.items.make import Make
from specifications.enums.pressure_switch import BreaksOn, ResetType
from specifications.enums.unit import Unit
from specifications.doc import Doc
from specifications.item import Item
from specifications.items.low_gas_pressure_switch import LowGasPressureSwitch
from specifications.items.pipe_size import PipeSize
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class LowAirPressureSwitch(Item):
    item_group = ItemGroup.equipment

    smd_2 = None
    smd_3 = None
    hb40a214 = None
    afs_a = None
    dietz_161P = None
    c645d1003 = None
    c645d1011 = None
    c645d1029 = None
    c645d1037 = None
    c645d1045 = None
    c645d1052 = None
    c645d1060 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, breaks_on: BreaksOn, range_min, range_max, range_unit: Unit,
                 reset_type: ResetType, size: PipeSize, manual: str = None, part_number=None,
                 honeywell_replacement=None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.part_number = Spec("Part Number", part_number)
        self.breaks_on = Spec("Breaks on", breaks_on)
        self.range = [range_min, range_max, range_unit]
        self.reset_type = Spec("Reset Type", reset_type)
        self.size = size

        # LowAirPressureSwitch
        self.honeywell_replacement = honeywell_replacement

        if manual:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, items):
        if items[0] and items[1] and items[2]:
            self._range = Spec("Range", f"{items[0]} - {items[1]}", items[2])
        else:
            self._range = Spec("Range", None)

    @item_property
    def size(self):
        return self._size

    @size.setter
    def size(self, item):
        self._size = Spec("Size", item, Unit.inch)

    @item_property
    def honeywell_replacement(self):
        return self._honeywell_replacement

    @honeywell_replacement.setter
    def honeywell_replacement(self, item):
        self._honeywell_replacement = Spec("Honeywell Replacement", item)

    def __str__(self):
        if self.part_number.value is None:
            return f"{self.model}"
        else:
            return f"{self.model} - {self.part_number}"


# Antunes
# LGP-A

LowAirPressureSwitch.smd_2 = LowAirPressureSwitch(Make.antunes, "SMD", BreaksOn.fall, 0.17, 6,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Antunes SMD manual.pdf", 8024204107)
LowAirPressureSwitch.smd_3 = LowAirPressureSwitch(Make.antunes, "SMD", BreaksOn.fall, 0.17, 12,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Antunes SMD manual.pdf", 8021206255)

# ASCO
# H-Series

LowAirPressureSwitch.hb40a214 = LowAirPressureSwitch(Make.asco, "H-Series", BreaksOn.fall, 4, 12,
                                                     Unit.pounds_per_square_inch, ResetType.auto, PipeSize.d0_25,
                                                     "Asco H Series manual.pdf", "HB40A214")

# Cleavland Controls
# AFS-A

LowAirPressureSwitch.afs_a = LowAirPressureSwitch(Make.cleveland_controls, "AFS-A", BreaksOn.fall, .05, 12,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Cleveland Controls AFS-A manual.pdf")

# Dietz
# 161P

LowAirPressureSwitch.dietz_161P = LowAirPressureSwitch(Make.cleveland_controls, "161P", BreaksOn.fall, .25, 15,
                                                       Unit.pounds_per_square_inch, ResetType.auto, PipeSize.d0_25,
                                                       "Dietz 161P manual.pdf")

# Honeywell
# C645D

LowAirPressureSwitch.c645d1003 = LowAirPressureSwitch(Make.honeywell, "C645D1003", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowAirPressureSwitch.c645d1011 = LowAirPressureSwitch(Make.honeywell, "C645D1011", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowAirPressureSwitch.c645d1029 = LowAirPressureSwitch(Make.honeywell, "C645D1029", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowAirPressureSwitch.c645d1037 = LowAirPressureSwitch(Make.honeywell, "C645D1037", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowAirPressureSwitch.c645d1045 = LowAirPressureSwitch(Make.honeywell, "C645D1045", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowAirPressureSwitch.c645d1052 = LowAirPressureSwitch(Make.honeywell, "C645D1052", BreaksOn.fall, 2, 20,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowAirPressureSwitch.c645d1060 = LowAirPressureSwitch(Make.honeywell, "C645D1060", BreaksOn.fall, 2, 20,
                                                      Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")

# Antunes.honeywell_replacement

LowAirPressureSwitch.smd_2.honeywell_replacement = LowGasPressureSwitch.a3004
LowAirPressureSwitch.smd_3.honeywell_replacement = LowGasPressureSwitch.a3004

# Asco.honeywell_replacement

LowAirPressureSwitch.hb40a214.honeywell_replacement = LowGasPressureSwitch.a3137

# Cleveland Controls. honeywell_replacement

LowAirPressureSwitch.afs_a.honeywell_replacement = LowGasPressureSwitch.a3053

# Dietz.honeywell_replacement

LowAirPressureSwitch.dietz_161P.honeywell_replacement = LowGasPressureSwitch.a3137

# Honeywell.honeywell_replacement

LowAirPressureSwitch.c645d1003.honeywell_replacement = LowGasPressureSwitch.a3053
LowAirPressureSwitch.c645d1011.honeywell_replacement = LowGasPressureSwitch.a3053
LowAirPressureSwitch.c645d1029.honeywell_replacement = LowGasPressureSwitch.a3053
LowAirPressureSwitch.c645d1037.honeywell_replacement = LowGasPressureSwitch.a3053
LowAirPressureSwitch.c645d1045.honeywell_replacement = LowGasPressureSwitch.a3053
LowAirPressureSwitch.c645d1052.honeywell_replacement = LowGasPressureSwitch.a3053
LowAirPressureSwitch.c645d1060.honeywell_replacement = LowGasPressureSwitch.a3053

# for var in vars(LowAirPressureSwitch):
#     print(var)
