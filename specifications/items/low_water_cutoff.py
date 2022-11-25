from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
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
                 water_column: bool = None, pump_controller: bool = None, manual_reset: bool = None,
                 float_block: bool = None, max_differential: bool = None, alternative_tappings: bool = None,
                 single_pole_single_throw_switch: int or None = None,
                 single_pole_double_throw_switch: int or None = None,
                 integral_conductance_probe: int or None = None,
                 manual: str or None = None, parts_list: str or None = None, catalogue: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.part_number = Spec("Part Number", part_number)
        self.max_allowable_working_pressure = Spec("MAWP", max_allowable_working_pressure, mawp_unit)
        self.bolts = Spec("Bolts", bolts)
        # Bools
        self.water_column = Spec("Water Column", water_column)
        self.pump_controller = Spec("Pump Controller", pump_controller)
        self.manual_reset = Spec("Manual Reset", manual_reset)
        self.float_block = Spec("Float Block", float_block)
        self.max_differential = Spec("Max Differential", max_differential)
        self.alternative_tappings = Spec("Alternative Tappings", alternative_tappings)
        # qty
        self.single_pole_single_throw_switch = Spec("SPST qty", single_pole_single_throw_switch)
        self.single_pole_double_throw_switch = Spec("SPDT qty", single_pole_double_throw_switch)
        self.integral_conductance_probe = Spec("Integral Conductance Probe qty", integral_conductance_probe)

        if manual or parts_list or catalogue:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.parts_list = Spec("Parts List", Doc(parts_list))
        self.catalogue = Spec("Catalogue", Doc(catalogue))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

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
# 150S, 158S, 159S
LowWaterCutOff._150s = LowWaterCutOff(Make.mcdonnell_miller, "150S", "171702", 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=1,
                                      single_pole_double_throw_switch=1,
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")

LowWaterCutOff._150s_b = LowWaterCutOff(Make.mcdonnell_miller, "150S-B", "171903", 150, Unit.pounds_per_square_inch, 8,
                                        pump_controller=True,
                                        float_block=True,
                                        single_pole_single_throw_switch=1,
                                        single_pole_double_throw_switch=1,
                                        manual="McDonnell & Miller 150S 157S manual.pdf",
                                        parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                        catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._150s_b_m = LowWaterCutOff(Make.mcdonnell_miller, "150S-B-M", "172803", 150, Unit.pounds_per_square_inch,
                                          8,
                                          pump_controller=True,
                                          manual_reset=True,
                                          float_block=True,
                                          single_pole_single_throw_switch=1,
                                          single_pole_double_throw_switch=1,
                                          manual="McDonnell & Miller 150S 157S manual.pdf",
                                          parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                          catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._150s_bmd = LowWaterCutOff(Make.mcdonnell_miller, "150S-BMD", "172002", 150, Unit.pounds_per_square_inch,
                                          8,
                                          pump_controller=True,
                                          float_block=True,
                                          max_differential=True,
                                          single_pole_single_throw_switch=1,
                                          single_pole_double_throw_switch=1,
                                          manual="McDonnell & Miller 150S 157S manual.pdf",
                                          parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                          catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._150s_bm_md = LowWaterCutOff(Make.mcdonnell_miller, "150S-BM-MD", "172805", 150,
                                            Unit.pounds_per_square_inch, 8,
                                            pump_controller=True,
                                            manual_reset=True,
                                            float_block=True,
                                            max_differential=True,
                                            single_pole_single_throw_switch=1,
                                            single_pole_double_throw_switch=1,
                                            manual="McDonnell & Miller 150S 157S manual.pdf",
                                            parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                            catalogue="McDonnell & Miller 150S 157S catalogue.pdf")

LowWaterCutOff._150s_md = LowWaterCutOff(Make.mcdonnell_miller, "150S-MD", "171802", 150, Unit.pounds_per_square_inch,
                                         8,
                                         pump_controller=True,
                                         max_differential=True,
                                         single_pole_single_throw_switch=1,
                                         single_pole_double_throw_switch=1,
                                         manual="McDonnell & Miller 150S 157S manual.pdf",
                                         parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                         catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._150s_m = LowWaterCutOff(Make.mcdonnell_miller, "150S-M", "172806", 150, Unit.pounds_per_square_inch, 8,
                                        pump_controller=True,
                                        manual_reset=True,
                                        single_pole_single_throw_switch=1,
                                        single_pole_double_throw_switch=1,
                                        manual="McDonnell & Miller 150S 157S manual.pdf",
                                        parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                        catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._150s_m_md = LowWaterCutOff(Make.mcdonnell_miller, "150S-M-MD", "172807", 150,
                                           Unit.pounds_per_square_inch, 8,
                                           pump_controller=True,
                                           manual_reset=True,
                                           max_differential=True,
                                           single_pole_single_throw_switch=1,
                                           single_pole_double_throw_switch=1,
                                           manual="McDonnell & Miller 150S 157S manual.pdf",
                                           parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                           catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._158s = LowWaterCutOff(Make.mcdonnell_miller, "158S", "178402", 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      single_pole_double_throw_switch=2,
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._158s_m = LowWaterCutOff(Make.mcdonnell_miller, "158S-M", "172819", 150, Unit.pounds_per_square_inch, 8,
                                        pump_controller=True,
                                        manual_reset=True,
                                        single_pole_double_throw_switch=2,
                                        manual="McDonnell & Miller 150S 157S manual.pdf",
                                        parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                        catalogue="McDonnell & Miller 150S 157S catalogue.pdf")
LowWaterCutOff._159s = LowWaterCutOff(Make.mcdonnell_miller, "159S", "178802", 150, Unit.pounds_per_square_inch, 8,
                                      pump_controller=True,
                                      single_pole_single_throw_switch=2,
                                      manual="McDonnell & Miller 150S 157S manual.pdf",
                                      parts_list="McDonnell & Miller 150 150S 157 157S parts list.pdf",
                                      catalogue="McDonnell & Miller 150S 157S catalogue.pdf")


# 157S


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
