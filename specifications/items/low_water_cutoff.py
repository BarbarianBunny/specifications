from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.lwco_type import LWCOType
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

    def __init__(self, make: Make, model: str, lwco_type: LWCOType or None, max_allowable_working_pressure: int or None,
                 mawp_unit: Unit or None,
                 bolts: int or None,
                 mercury_switches: bool or None = None,
                 single_pole_single_throw_switch: int or None = None,
                 single_pole_double_throw_switch: int or None = None,
                 single_pole_double_break: int or None = None,
                 water_column: bool = None,
                 pump_controller: bool = None,
                 dual_pump_control: bool = None,
                 mcdonnell_miller_upgrade: Item = None,
                 sensor_probe: Item = None,
                 cb: str = None,
                 swa: str = None,
                 a: str = None,
                 a_b: str = None,
                 a_b_d_g: str = None,
                 a_r_rl: str = None,
                 b: str = None,
                 lqhu: str = None,
                 g: str = None,
                 _7b: str = None,
                 m: str = None,
                 bp: str = None,
                 md: str = None,
                 hw: str = None,
                 t: str = None,
                 mt: str = None,
                 _24_120: str = None,
                 number_suffix: str = None,
                 br_1: str = None,
                 lp: str = None,
                 hp: str = None,
                 s: str = None,
                 hd: str = None,
                 manual: str = None, parts_list: str = None, catalogue: str = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.lwco_type = Spec("Type", lwco_type)
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
        # Items
        self.mcdonnell_miller_upgrade = mcdonnell_miller_upgrade
        self.sensor_probe = sensor_probe

        # Prefix
        if cb or swa:
            self.prefix_header = Spec(None, Heading("Model Prefixes"))
        self.cb = Spec("CB", cb)
        self.swa = Spec("SWA", swa)

        # Suffix
        if a or a_b or a_b_d_g or a_r_rl or b or lqhu or g or _7b or m or bp or md or hw or t or mt or _24_120 or \
                number_suffix or br_1 or lp or hp or s or hd:
            self.suffix_header = Spec(None, Heading("Model Suffixes"))
        self.a = Spec("A", a)
        self.a_b = Spec("A or B", a_b)
        self.a_b_d_g = Spec("A, B, D, or G", a_b_d_g)
        self.a_r_rl = Spec("A, R, or RL", a_r_rl)
        self.b = Spec("B", b)
        self.lqhu = Spec("LQHU", lqhu)
        self.g = Spec("G", g)
        self._7b = Spec("7B", _7b)
        self.m = Spec("M", m)
        self.bp = Spec("BP", bp)
        self.md = Spec("MD", md)
        self.hw = Spec("HW", hw)
        self.t = Spec("T", t)
        self.mt = Spec("MT", mt)
        self._24_120 = Spec("24 or 120", _24_120)
        self.number_suffix = Spec("1, 2, 3, 4, or 5", number_suffix)
        self.br_1 = Spec("BR-1", br_1)
        self.lp = Spec("LP", lp)
        self.hp = Spec("HP", hp)
        self.s = Spec("S", s)
        self.hd = Spec("HD", hd)

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

    @item_property
    def sensor_probe(self):
        return self._sensor_probe

    @sensor_probe.setter
    def sensor_probe(self, item):
        self._sensor_probe = Spec("Sensor/Probe", item)

    def __str__(self):
        return f"{self.model}"


# Cleaver Brooks
LowWaterCutOff.level_master_750_193 = LowWaterCutOff(Make.cleaver_brooks, "750-193 Level Master", LWCOType.float, 250,
                                                     Unit.pounds_per_square_inch, None,
                                                     manual="Cleaver Brooks 750-193 Level Master manual.pdf")
LowWaterCutOff.level_master_750_281 = LowWaterCutOff(Make.cleaver_brooks, "750-281 Level Master", LWCOType.float, 250,
                                                     Unit.pounds_per_square_inch, None,
                                                     manual="Cleaver Brooks 750-281 Level Master manual.pdf")

# McDonnell & Miller
# 150S
LowWaterCutOff._150s = LowWaterCutOff(Make.mcdonnell_miller, "150S", LWCOType.float, 150, Unit.pounds_per_square_inch,
                                      8,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=1,
                                      single_pole_double_throw_switch=1,
                                      swa="Replacement Switch Assembly only",
                                      b="Float Block",
                                      m="Manual Reset",
                                      md="Max Differential",
                                      hd="Replacement Head only",
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 150
LowWaterCutOff._150 = LowWaterCutOff(Make.mcdonnell_miller, "150", LWCOType.float, 150, Unit.pounds_per_square_inch, 8,
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
LowWaterCutOff._158s = LowWaterCutOff(Make.mcdonnell_miller, "158S", LWCOType.float, 150, Unit.pounds_per_square_inch,
                                      8,
                                      pump_controller=True,
                                      single_pole_double_throw_switch=2,
                                      swa="Replacement Switch Assembly only",
                                      m="Manual Reset",
                                      hd="Replacement Head only",
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 159S
LowWaterCutOff._159s = LowWaterCutOff(Make.mcdonnell_miller, "159S", LWCOType.float, 150, Unit.pounds_per_square_inch,
                                      8,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=2,
                                      swa="Replacement Switch Assembly only",
                                      hd="Replacement Head only",
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 157S
LowWaterCutOff._157s = LowWaterCutOff(Make.mcdonnell_miller, "157S", LWCOType.float, 150, Unit.pounds_per_square_inch,
                                      8,
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
LowWaterCutOff._157 = LowWaterCutOff(Make.mcdonnell_miller, "157", LWCOType.float, 150, Unit.pounds_per_square_inch, 8,
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
LowWaterCutOff._150e = LowWaterCutOff(Make.mcdonnell_miller, "150E", LWCOType.float, 150, Unit.pounds_per_square_inch,
                                      8,
                                      pump_controller=True,
                                      dual_pump_control=True,
                                      m="Manual Reset",
                                      manual="McDonnell & Miller 150E 157E manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
# 157E
LowWaterCutOff._157e = LowWaterCutOff(Make.mcdonnell_miller, "157E", LWCOType.float, 150, Unit.pounds_per_square_inch,
                                      8,
                                      water_column=True,
                                      pump_controller=True,
                                      dual_pump_control=True,
                                      m="Manual Reset",
                                      manual="McDonnell & Miller 150E 157E manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")

# 61
LowWaterCutOff._61 = LowWaterCutOff(Make.mcdonnell_miller, "61", LWCOType.float, 20, Unit.pounds_per_square_inch, 4,
                                    single_pole_single_throw_switch=2,
                                    manual="McDonnell & Miller 61 manual.pdf",
                                    parts_list="McDonnell & Miller 61 parts list.pdf",
                                    catalogue="McDonnell & Miller 61 catalogue.pdf")

# 63
LowWaterCutOff._63 = LowWaterCutOff(Make.mcdonnell_miller, "63", LWCOType.float, 50, Unit.pounds_per_square_inch, 4,
                                    single_pole_double_throw_switch=1,
                                    b="Float Block",
                                    m="Manual Reset",
                                    manual="McDonnell & Miller 63 manual.pdf",
                                    parts_list="McDonnell & Miller 63 parts list.pdf",
                                    catalogue="McDonnell & Miller 63 catalogue.pdf")

# 64
LowWaterCutOff._64 = LowWaterCutOff(Make.mcdonnell_miller, "64", LWCOType.float, 50, Unit.pounds_per_square_inch, 4,
                                    single_pole_single_throw_switch=2,
                                    a="Quick Hook-up Fittings",
                                    b="Float Block",
                                    manual="McDonnell & Miller 64 manual.pdf",
                                    parts_list="McDonnell & Miller 64 parts list.pdf",
                                    catalogue="McDonnell & Miller 64 catalogue.pdf")

# 67
LowWaterCutOff._67 = LowWaterCutOff(Make.mcdonnell_miller, "67", LWCOType.float, 20, Unit.pounds_per_square_inch, None,
                                    single_pole_single_throw_switch=2,
                                    g="For Millivolt Service",
                                    lqhu="Without Quick Hook-up Fittings",
                                    manual="McDonnell & Miller 67 767 manual.pdf",
                                    parts_list="McDonnell & Miller 67 parts list.pdf",
                                    catalogue="McDonnell & Miller 67 catalogue.pdf")

# RS
LowWaterCutOff.rs = LowWaterCutOff(Make.mcdonnell_miller, "RS", LWCOType.sensor, None, Unit.pounds_per_square_inch,
                                   None,
                                   number_suffix="Number of Probes",
                                   br_1="250 psi (Probes Ordered Separately)",
                                   lp="15 psi Steam, 160 psi Hot Water",
                                   hp="250 psi",
                                   s="Short Probe",
                                   manual="McDonnell & Miller 750 manual.pdf",
                                   parts_list="McDonnell & Miller RS parts list.pdf",
                                   catalogue="McDonnell & Miller RS catalogue.pdf")
# 750
LowWaterCutOff._750 = LowWaterCutOff(Make.mcdonnell_miller, "750", LWCOType.controller, None, None, None,
                                     sensor_probe=LowWaterCutOff.rs,
                                     hw="High Water Cutoff Only",
                                     t="Auto Reset",
                                     mt="Manual Reset",
                                     _24_120="Voltage",
                                     manual="McDonnell & Miller 750 manual.pdf",
                                     catalogue="McDonnell & Miller 750 catalogue.pdf")

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
