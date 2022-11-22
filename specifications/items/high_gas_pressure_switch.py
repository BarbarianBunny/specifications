from specifications.items.make import Make
from specifications.enums.pressure_switch import ResetType, BreaksOn
from specifications.enums.unit import Unit
from specifications.doc import Doc
from specifications.item import Item
from specifications.items.pipe_size import PipeSize
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class HighGasPressureSwitch(Item):
    hgp_a_1 = None
    hgp_a_2 = None
    hgp_a_3 = None
    hgp_g_2 = None
    hgp_g_3 = None
    hgp_g_7 = None
    b1002 = None
    b1028 = None
    b1051 = None
    b1085 = None
    b1101 = None
    b1119 = None
    b3002 = None
    b3028 = None
    b3051 = None
    b3085 = None
    b3101 = None
    b3119 = None
    c645b1005 = None
    c645b1013 = None
    c645b1021 = None
    c645b1039 = None
    c645b1047 = None
    c645b1054 = None
    c645b1062 = None
    c645b1070 = None
    c645b1088 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, breaks_on: BreaksOn, range_min, range_max, range_unit: Unit,
                 reset_type: ResetType, size: PipeSize, manual: str = None, part_number=None, honeywell_replacement=None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.part_number = Spec("Part Number", part_number)
        self.breaks_on = Spec("Breaks on", breaks_on)
        self.range = Spec("Range", f"{range_min} - {range_max}", range_unit)
        self.reset_type = Spec("Reset Type", reset_type)
        self.size = size

        # LowGasPressureSwitch
        self.honeywell_replacement = honeywell_replacement

        # Docs
        self.manual = Spec("Manual", Doc(manual))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

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
# HGP-A

HighGasPressureSwitch.hgp_a_1 = HighGasPressureSwitch(Make.antunes, "HGP-A", BreaksOn.rise, 2, 16,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Antunes Model A manual.pdf", 803112601)
HighGasPressureSwitch.hgp_a_2 = HighGasPressureSwitch(Make.antunes, "HGP-A", BreaksOn.rise, 5, 28,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Antunes Model A manual.pdf", 803112602)
HighGasPressureSwitch.hgp_a_3 = HighGasPressureSwitch(Make.antunes, "HGP-A", BreaksOn.rise, 10, 50,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Antunes Model A manual.pdf", 803112603)

# HGP-G

HighGasPressureSwitch.hgp_g_2 = HighGasPressureSwitch(Make.antunes, "HGP-G", BreaksOn.rise, 2, 20,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Antunes Model G manual.pdf", 8101111202)
HighGasPressureSwitch.hgp_g_3 = HighGasPressureSwitch(Make.antunes, "HGP-G", BreaksOn.rise, 8, 35,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Antunes Model G manual.pdf", 8101111303)
HighGasPressureSwitch.hgp_g_7 = HighGasPressureSwitch(Make.antunes, "HGP-G", BreaksOn.rise, 10, 60,
                                                      Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                      "Antunes Model G manual.pdf", 8101111407)

# Honeywell
# C645B

HighGasPressureSwitch.c645b1005 = HighGasPressureSwitch(Make.honeywell, "C645B1005", BreaksOn.rise, 3, 21,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1013 = HighGasPressureSwitch(Make.honeywell, "C645B1013", BreaksOn.rise, 3, 21,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1021 = HighGasPressureSwitch(Make.honeywell, "C645B1021", BreaksOn.rise, 3, 21,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1039 = HighGasPressureSwitch(Make.honeywell, "C645B1039", BreaksOn.rise, 5, 35,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1047 = HighGasPressureSwitch(Make.honeywell, "C645B1047", BreaksOn.rise, 3, 21,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1054 = HighGasPressureSwitch(Make.honeywell, "C645B1054", BreaksOn.rise, .7, 5.0,
                                                        Unit.kpa, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1062 = HighGasPressureSwitch(Make.honeywell, "C645B1062", BreaksOn.rise, 5, 35,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1070 = HighGasPressureSwitch(Make.honeywell, "C645B1070", BreaksOn.rise, 10, 45,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")
HighGasPressureSwitch.c645b1088 = HighGasPressureSwitch(Make.honeywell, "C645B1088", BreaksOn.rise, 3, 21,
                                                        Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                        "Honeywell C645x manual.pdf")

# C6097B1xxx

HighGasPressureSwitch.b1002 = HighGasPressureSwitch(Make.honeywell, "C6097B1002", BreaksOn.rise, 10, 60,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Honeywell C6097x1xxx manual.pdf")
HighGasPressureSwitch.b1028 = HighGasPressureSwitch(Make.honeywell, "C6097B1028", BreaksOn.rise, 3, 21,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Honeywell C6097x1xxx manual.pdf")
HighGasPressureSwitch.b1051 = HighGasPressureSwitch(Make.honeywell, "C6097B1051", BreaksOn.rise, 1.5, 7,
                                                    Unit.pound_per_square_inch, ResetType.manual, PipeSize.d0_25,
                                                    "Honeywell C6097x1xxx manual.pdf")
HighGasPressureSwitch.b1085 = HighGasPressureSwitch(Make.honeywell, "C6097B1085", BreaksOn.rise, 12, 60,
                                                    Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                    "Honeywell C6097x1xxx manual.pdf")
HighGasPressureSwitch.b1101 = HighGasPressureSwitch(Make.honeywell, "C6097B1101", BreaksOn.rise, 1.5, 7,
                                                    Unit.pound_per_square_inch, ResetType.auto, PipeSize.d0_25,
                                                    "Honeywell C6097x1xxx manual.pdf")
HighGasPressureSwitch.b1119 = HighGasPressureSwitch(Make.honeywell, "C6097B1119", BreaksOn.rise, 3, 21,
                                                    Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                    "Honeywell C6097x1xxx manual.pdf")

# C6097B3xxx

HighGasPressureSwitch.b3002 = HighGasPressureSwitch(Make.honeywell, "C6097B3002", BreaksOn.rise, 12, 60,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Honeywell C6097x3xxx manual.pdf")
HighGasPressureSwitch.b3028 = HighGasPressureSwitch(Make.honeywell, "C6097B3028", BreaksOn.rise, 1, 20,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Honeywell C6097x3xxx manual.pdf")
HighGasPressureSwitch.b3051 = HighGasPressureSwitch(Make.honeywell, "C6097B3051", BreaksOn.rise, 40, 200,
                                                    Unit.inches_of_water_column, ResetType.manual, PipeSize.d0_25,
                                                    "Honeywell C6097x3xxx manual.pdf")
HighGasPressureSwitch.b3085 = HighGasPressureSwitch(Make.honeywell, "C6097B3085", BreaksOn.rise, 12, 60,
                                                    Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                    "Honeywell C6097x3xxx manual.pdf")
HighGasPressureSwitch.b3101 = HighGasPressureSwitch(Make.honeywell, "C6097B3101", BreaksOn.rise, 40, 200,
                                                    Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                    "Honeywell C6097x3xxx manual.pdf")
HighGasPressureSwitch.b3119 = HighGasPressureSwitch(Make.honeywell, "C6097B3119", BreaksOn.rise, 1, 20,
                                                    Unit.inches_of_water_column, ResetType.auto, PipeSize.d0_25,
                                                    "Honeywell C6097x3xxx manual.pdf")

# Antunes.honeywell_replacement

HighGasPressureSwitch.hgp_a_1.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.hgp_a_2.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.hgp_a_3.honeywell_replacement = HighGasPressureSwitch.b3002

HighGasPressureSwitch.hgp_g_2.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.hgp_g_3.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.hgp_g_7.honeywell_replacement = HighGasPressureSwitch.b3002

# Honeywell.honeywell_replacement

HighGasPressureSwitch.c645b1005.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.c645b1013.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.c645b1021.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.c645b1039.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.c645b1047.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.c645b1054.honeywell_replacement = HighGasPressureSwitch.b3002
HighGasPressureSwitch.c645b1062.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.c645b1070.honeywell_replacement = HighGasPressureSwitch.b3002
HighGasPressureSwitch.c645b1088.honeywell_replacement = HighGasPressureSwitch.b3028

HighGasPressureSwitch.b1002.honeywell_replacement = HighGasPressureSwitch.b3002
HighGasPressureSwitch.b1028.honeywell_replacement = HighGasPressureSwitch.b3028
HighGasPressureSwitch.b1051.honeywell_replacement = HighGasPressureSwitch.b3051
HighGasPressureSwitch.b1085.honeywell_replacement = HighGasPressureSwitch.b3085
HighGasPressureSwitch.b1101.honeywell_replacement = HighGasPressureSwitch.b3101
HighGasPressureSwitch.b1119.honeywell_replacement = HighGasPressureSwitch.b3119

# for var in vars(HighGasPressureSwitch):
#     print(var)
