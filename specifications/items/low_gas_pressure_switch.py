from specifications.enums.item_group import ItemGroup
from specifications.header import Header
from specifications.items.make import Make
from specifications.enums.pressure_switch import BreaksOn, ResetType
from specifications.enums.unit import Unit
from specifications.doc import Doc
from specifications.item import Item
from specifications.items.pipe_size import PipeSize
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class LowGasPressureSwitch(Item):
    item_group = ItemGroup.equipment

    lgp_a_1 = None
    lgp_a_9 = None
    lgp_a_2 = None
    lgp_a_3 = None
    lgp_a_4 = None
    lgp_g_1 = None
    lgp_g_2 = None
    lgp_g_3 = None
    lgp_g_7 = None
    a1004 = None
    a1012 = None
    a1038 = None
    a1053 = None
    a1079 = None
    a1095 = None
    a1111 = None
    a1137 = None
    a3004 = None
    a3012 = None
    a3038 = None
    a3053 = None
    a3079 = None
    a3095 = None
    a3111 = None
    a3137 = None
    c645a1006 = None
    c645a1014 = None
    c645a1022 = None
    c645a1030 = None
    c645a1048 = None
    c645a1055 = None
    c645a1063 = None
    c645a1071 = None
    c645a1089 = None
    c645a1097 = None
    c645a1105 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, breaks_on: BreaksOn, range_min, range_max, range_unit: Unit,
                 reset_type: ResetType, size: PipeSize,  manual: str = None, part_number=None, honeywell_replacement=None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.part_number = Spec("Part Number", part_number)
        self.breaks_on = Spec("Breaks on", breaks_on)
        self.range = [range_min, range_max, range_unit]
        self.reset_type = Spec("Reset Type", reset_type)
        self.size = size

        # LowGasPressureSwitch
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

LowGasPressureSwitch.lgp_a_1 = LowGasPressureSwitch(Make.antunes, "LGP-A", BreaksOn.fall, 1, 6,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model A manual.pdf", 803112501)
LowGasPressureSwitch.lgp_a_9 = LowGasPressureSwitch(Make.antunes, "LGP-A", BreaksOn.fall, 1, 35,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model A manual.pdf", 803112509)
LowGasPressureSwitch.lgp_a_2 = LowGasPressureSwitch(Make.antunes, "LGP-A", BreaksOn.fall, 2, 14,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model A manual.pdf", 803112502)
LowGasPressureSwitch.lgp_a_3 = LowGasPressureSwitch(Make.antunes, "LGP-A", BreaksOn.fall, 6, 24,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model A manual.pdf", 803112503)
LowGasPressureSwitch.lgp_a_4 = LowGasPressureSwitch(Make.antunes, "LGP-A", BreaksOn.fall, 10, 50,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model A manual.pdf", 803112504)

# LGP-G

LowGasPressureSwitch.lgp_g_1 = LowGasPressureSwitch(Make.antunes, "LGP-G", BreaksOn.fall, 0.5, 4,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model G manual.pdf", 8103116101)
LowGasPressureSwitch.lgp_g_2 = LowGasPressureSwitch(Make.antunes, "LGP-G", BreaksOn.fall, 1, 20,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model G manual.pdf", 8103116202)
LowGasPressureSwitch.lgp_g_3 = LowGasPressureSwitch(Make.antunes, "LGP-G", BreaksOn.fall, 5, 30,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model G manual.pdf", 8103116303)
LowGasPressureSwitch.lgp_g_7 = LowGasPressureSwitch(Make.antunes, "LGP-G", BreaksOn.fall, 7, 55,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Antunes Model G manual.pdf", 8103116407)

# Honeywell
# C645A

LowGasPressureSwitch.c645a1006 = LowGasPressureSwitch(Make.honeywell, "C645A1006", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1014 = LowGasPressureSwitch(Make.honeywell, "C645A1014", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1022 = LowGasPressureSwitch(Make.honeywell, "C645A1022", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1030 = LowGasPressureSwitch(Make.honeywell, "C645A1030", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1048 = LowGasPressureSwitch(Make.honeywell, "C645A1048", BreaksOn.fall, 5, 35,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1055 = LowGasPressureSwitch(Make.honeywell, "C645A1055", BreaksOn.fall, 5, 35,
                                                      Unit.kilopascal, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1063 = LowGasPressureSwitch(Make.honeywell, "C645A1063", BreaksOn.fall, 5, 35,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1071 = LowGasPressureSwitch(Make.honeywell, "C645A1071", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1089 = LowGasPressureSwitch(Make.honeywell, "C645A1089", BreaksOn.fall, 0.7, 5.0,
                                                      Unit.kilopascal, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1097 = LowGasPressureSwitch(Make.honeywell, "C645A1097", BreaksOn.fall, 0.7, 5.0,
                                                      Unit.kilopascal, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")
LowGasPressureSwitch.c645a1105 = LowGasPressureSwitch(Make.honeywell, "C645A1105", BreaksOn.fall, 3, 21,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Honeywell C645x manual.pdf")

# C6097A1xxx

LowGasPressureSwitch.a1004 = LowGasPressureSwitch(Make.honeywell, "C6097A1004", BreaksOn.fall, 0.4, 5,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1012 = LowGasPressureSwitch(Make.honeywell, "C6097A1012", BreaksOn.fall, 3, 21,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1038 = LowGasPressureSwitch(Make.honeywell, "C6097A1038", BreaksOn.fall, 12, 60,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1053 = LowGasPressureSwitch(Make.honeywell, "C6097A1053", BreaksOn.fall, 3, 21,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1079 = LowGasPressureSwitch(Make.honeywell, "C6097A1079", BreaksOn.fall, 12, 60,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1095 = LowGasPressureSwitch(Make.honeywell, "C6097A1095", BreaksOn.fall, 0.4, 5,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1111 = LowGasPressureSwitch(Make.honeywell, "C6097A1111", BreaksOn.fall, 1.5, 7,
                                                  Unit.pounds_per_square_inch, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")
LowGasPressureSwitch.a1137 = LowGasPressureSwitch(Make.honeywell, "C6097A1137", BreaksOn.fall, 1.5, 7,
                                                  Unit.pounds_per_square_inch, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x1xxx manual.pdf")

# C6097A3xxx

LowGasPressureSwitch.a3004 = LowGasPressureSwitch(Make.honeywell, "C6097A3004", BreaksOn.fall, 0.4, 4,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3012 = LowGasPressureSwitch(Make.honeywell, "C6097A3012", BreaksOn.fall, 1, 20,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3038 = LowGasPressureSwitch(Make.honeywell, "C6097A3038", BreaksOn.fall, 12, 60,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3053 = LowGasPressureSwitch(Make.honeywell, "C6097A3053", BreaksOn.fall, 1, 20,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3079 = LowGasPressureSwitch(Make.honeywell, "C6097A3079", BreaksOn.fall, 12, 60,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3095 = LowGasPressureSwitch(Make.honeywell, "C6097A3095", BreaksOn.fall, 0.4, 4,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3111 = LowGasPressureSwitch(Make.honeywell, "C6097A3111", BreaksOn.fall, 40, 200,
                                                  Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")
LowGasPressureSwitch.a3137 = LowGasPressureSwitch(Make.honeywell, "C6097A3137", BreaksOn.fall, 40, 200,
                                                  Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                  "Honeywell C6097x3xxx manual.pdf")

# Antunes.honeywell_replacement

LowGasPressureSwitch.lgp_a_1.honeywell_replacement = LowGasPressureSwitch.a3095
LowGasPressureSwitch.lgp_a_9.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.lgp_a_2.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.lgp_a_3.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.lgp_a_4.honeywell_replacement = LowGasPressureSwitch.a3038
LowGasPressureSwitch.lgp_g_1.honeywell_replacement = LowGasPressureSwitch.a3095
LowGasPressureSwitch.lgp_g_2.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.lgp_g_3.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.lgp_g_7.honeywell_replacement = LowGasPressureSwitch.a3038

# Honeywell.honeywell_replacement

LowGasPressureSwitch.c645a1006.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1014.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1022.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1030.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1048.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1055.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1063.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1071.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.c645a1089.honeywell_replacement = LowGasPressureSwitch.a3038
LowGasPressureSwitch.c645a1097.honeywell_replacement = LowGasPressureSwitch.a3038
LowGasPressureSwitch.c645a1105.honeywell_replacement = LowGasPressureSwitch.a3012

LowGasPressureSwitch.a1004.honeywell_replacement = LowGasPressureSwitch.a3004
LowGasPressureSwitch.a1012.honeywell_replacement = LowGasPressureSwitch.a3012
LowGasPressureSwitch.a1038.honeywell_replacement = LowGasPressureSwitch.a3038
LowGasPressureSwitch.a1053.honeywell_replacement = LowGasPressureSwitch.a3053
LowGasPressureSwitch.a1079.honeywell_replacement = LowGasPressureSwitch.a3079
LowGasPressureSwitch.a1095.honeywell_replacement = LowGasPressureSwitch.a3095
LowGasPressureSwitch.a1111.honeywell_replacement = LowGasPressureSwitch.a3111
LowGasPressureSwitch.a1137.honeywell_replacement = LowGasPressureSwitch.a3137

# for var in vars(LowGasPressureSwitch):
#     print(var)