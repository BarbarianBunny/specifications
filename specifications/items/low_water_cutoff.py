from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.heading import Heading
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class LowWaterCutOff(Item):
    item_group = ItemGroup.equipment

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, part_number: str or int, max_allowable_working_pressure, mawp_unit: Unit,
                 bolts: int or None,
                 mercury_switches: bool or None = None,
                 single_pole_single_throw_switch: int or None = None,
                 single_pole_double_throw_switch: int or None = None,
                 single_pole_double_break: int or None = None,
                 water_column: bool = None,
                 pump_controller: bool = None,
                 dual_pump_control: bool = None,
                 mcdonnell_miller_upgrade: Item = None,
                 b: str or None = None,
                 a: str or None = None,
                 a_b: str or None = None,
                 a_b_d_g: str or None = None,
                 a_r_rl: str or None = None,
                 _7b: str or None = None,
                 m: str or None = None,
                 bp: str or None = None,
                 md: str or None = None,
                 manual: str or None = None, parts_list: str or None = None, catalogue: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.part_number = Spec("Part Number", part_number)
        self.max_allowable_working_pressure = Spec("MAWP", max_allowable_working_pressure, mawp_unit)
        self.bolts = Spec("Bolts", bolts)
        # switches
        self.single_pole_single_throw_switch = Spec("SPST", single_pole_single_throw_switch)
        self.single_pole_double_throw_switch = Spec("SPDT", single_pole_double_throw_switch)
        self.single_pole_double_break = Spec("SPDB", single_pole_double_break)

        # Bools
        self.mercury_switches = Spec("Mercury Switches", mercury_switches)
        self.water_column = Spec("Water Column", water_column)
        self.pump_controller = Spec("Pump Controller", pump_controller)
        self.dual_pump_control = Spec("Dual Pump Control", dual_pump_control)
        # Replacement/upgrade
        self.mcdonnell_miller_upgrade = mcdonnell_miller_upgrade

        # Suffix
        if m or b or md or a_r_rl or bp:
            self.suffix_header = Spec(None, Heading("Model Suffixes"))
        self.b = Spec("B", b)
        self.a = Spec("A", a)
        self.a_b = Spec("A or B", a_b)
        self.a_b_d_g = Spec("A, B, D, or G", a_b_d_g)
        self.a_r_rl = Spec("A, R, or RL", a_r_rl)
        self._7b = Spec("7B", _7b)
        self.m = Spec("M", m)
        self.bp = Spec("BP", bp)
        self.md = Spec("MD", md)

        # Docs
        if manual or parts_list or catalogue:
            self.doc_header = Spec(None, Heading("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.parts_list = Spec("Parts List", Doc(parts_list))
        self.catalogue = Spec("Catalogue", Doc(catalogue))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    @item_property
    def mcdonnell_miller_upgrade(self):
        return self._mcdonnell_miller_upgrade

    @mcdonnell_miller_upgrade.setter
    def mcdonnell_miller_upgrade(self, item):
        self._mcdonnell_miller_upgrade = Spec("McDonnell & Miller Upgrade", item)

    def __str__(self):
        return f"{self.model}"


# Cleaver Brooks
LowWaterCutOff.level_master_750_193 = LowWaterCutOff(Make.cleaver_brooks, "750-193 Level Master", None, 250,
                                                     Unit.pounds_per_square_inch, None,
                                                     manual="Cleaver Brooks 750-193 Level Master manual.pdf")
LowWaterCutOff.level_master_750_281 = LowWaterCutOff(Make.cleaver_brooks, "750-281 Level Master", None, 250,
                                                     Unit.pounds_per_square_inch, None,
                                                     manual="Cleaver Brooks 750-281 Level Master manual.pdf")

# McDonnell & Miller
# 150S
LowWaterCutOff._150s = LowWaterCutOff(Make.mcdonnell_miller, "150S", None, 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=1,
                                      single_pole_double_throw_switch=1,
                                      b="Float Block",
                                      m="Manual Reset",
                                      md="Max Differential",
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 150
LowWaterCutOff._150 = LowWaterCutOff(Make.mcdonnell_miller, "150", None, 150, Unit.pounds_per_square_inch, 8,
                                     mercury_switches=True,
                                     pump_controller=True,
                                     single_pole_single_throw_switch=1,
                                     single_pole_double_throw_switch=1,
                                     mcdonnell_miller_upgrade=LowWaterCutOff._150s,
                                     b="Float Block",
                                     m="Manual Reset",
                                     md="Max Differential",
                                     manual="McDonnell & Miller 150S 157S manual.pdf",
                                     parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                     catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 158S
LowWaterCutOff._158s = LowWaterCutOff(Make.mcdonnell_miller, "158S", None, 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      single_pole_double_throw_switch=2,
                                      m="Manual Reset",
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 159S
LowWaterCutOff._159s = LowWaterCutOff(Make.mcdonnell_miller, "159S", None, 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=2,
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 157S
LowWaterCutOff._157s = LowWaterCutOff(Make.mcdonnell_miller, "157S", None, 150, Unit.pounds_per_square_inch, 8,
                                      water_column=True,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=1,
                                      single_pole_double_throw_switch=1,
                                      a_r_rl="Alternative Tappings",
                                      m="Manual Reset",
                                      md="Max Differential",
                                      bp="2 Integral Conductance Probes",
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 157
LowWaterCutOff._157 = LowWaterCutOff(Make.mcdonnell_miller, "157", None, 150, Unit.pounds_per_square_inch, 8,
                                     mercury_switches=True,
                                     water_column=True,
                                     pump_controller=True,
                                     single_pole_single_throw_switch=1,
                                     single_pole_double_throw_switch=1,
                                     mcdonnell_miller_upgrade=LowWaterCutOff._157s,
                                     a_r_rl="Alternative Tappings",
                                     m="Manual Reset",
                                     md="Max Differential",
                                     bp="2 Integral Conductance Probes",
                                     manual="McDonnell & Miller 150S 157S manual.pdf",
                                     parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                     catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 150E
LowWaterCutOff._150e = LowWaterCutOff(Make.mcdonnell_miller, "150E", None, 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      dual_pump_control=True,
                                      m="Manual Reset",
                                      manual="McDonnell & Miller 150E 157E manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 157E
LowWaterCutOff._157e = LowWaterCutOff(Make.mcdonnell_miller, "157E", None, 150, Unit.pounds_per_square_inch, 8,
                                      water_column=True,
                                      pump_controller=True,
                                      dual_pump_control=True,
                                      m="Manual Reset",
                                      manual="McDonnell & Miller 150E 157E manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")

# 61
LowWaterCutOff._61 = LowWaterCutOff(Make.mcdonnell_miller, "61", None, 20, Unit.pounds_per_square_inch, 4,
                                    single_pole_single_throw_switch=2,
                                    manual="McDonnell & Miller 61 manual.pdf",
                                    parts_list="McDonnell & Miller 61 parts list.pdf",
                                    catalogue="McDonnell & Miller 61 catalogue.pdf")

# 63


# 93
LowWaterCutOff._93 = LowWaterCutOff(Make.mcdonnell_miller, "93", None, 150, Unit.pounds_per_square_inch, 8,
                                    pump_controller=True,
                                    single_pole_double_break=1,
                                    _7b="7B Switch (Proportional Control)",
                                    m="Manual Reset",
                                    manual="McDonnell & Miller 93 193 94 194 manual.pdf",
                                    parts_list="McDonnell & Miller 93 193 parts list.pdf",
                                    catalogue="McDonnell & Miller 93 94 catalogue.pdf")
# 193
LowWaterCutOff._193 = LowWaterCutOff(Make.mcdonnell_miller, "193", None, 150, Unit.pounds_per_square_inch, 8,
                                     pump_controller=True,
                                     water_column=True,
                                     single_pole_double_break=1,
                                     a_b_d_g="Alternative Tappings",
                                     _7b="7B Switch (Proportional Control)",
                                     m="Manual Reset",
                                     manual="McDonnell & Miller 93 193 94 194 manual.pdf",
                                     parts_list="McDonnell & Miller 93 193 parts list.pdf",
                                     catalogue="McDonnell & Miller 193 194 catalogue.pdf")

# 94
LowWaterCutOff._94 = LowWaterCutOff(Make.mcdonnell_miller, "94", None, 250, Unit.pounds_per_square_inch, 10,
                                    pump_controller=True,
                                    single_pole_double_break=1,
                                    a="Alternative tappings",
                                    _7b="7B Switch (Proportional Control)",
                                    m="Manual Reset",
                                    manual="McDonnell & Miller 93 193 94 194 manual.pdf",
                                    parts_list="McDonnell & Miller 94 194 parts list.pdf",
                                    catalogue="McDonnell & Miller 93 94 catalogue.pdf")
# 194
LowWaterCutOff._194 = LowWaterCutOff(Make.mcdonnell_miller, "194", None, 250, Unit.pounds_per_square_inch, 10,
                                     pump_controller=True,
                                     water_column=True,
                                     single_pole_double_break=1,
                                     a_b="Alternative Tappings",
                                     _7b="7B Switch (Proportional Control)",
                                     m="Manual Reset",
                                     manual="McDonnell & Miller 93 193 94 194 manual.pdf",
                                     parts_list="McDonnell & Miller 94 194 parts list.pdf",
                                     catalogue="McDonnell & Miller 193 194 catalogue.pdf")

# LowWaterCutOff. = LowWaterCutOff(Make.mcdonnell_miller, "MODEL", "PART_NO", 150, Unit.pounds_per_square_inch, 8,
#                                  water_column=,
#                                  pump_controller=,
#                                  manual_reset=,
#                                  float_block=,
#                                  max_differential=,
#                                  alternative_tappings=,
#                                  single_pole_single_throw_switch=,
#                                  single_pole_double_throw_switch=,
#                                  integral_conductance_probe=,
#                                  manual="MANUAL",
#                                  parts_list="PARTS_LIST",
#                                  catalogue="CATALOGUE")

# for var in vars(Blank):
#     print(var)
