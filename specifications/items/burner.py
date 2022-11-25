from specifications.doc import Doc
from specifications.enums.fuel import Fuel
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Burner(Item):
    item_group = ItemGroup.equipment

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str or None, gas_type: Fuel or None, oil_type: Fuel or None,
                 manual: str or None, parts_list: str or None, datasheet: str or None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.gas_type = Spec("Gas Type", gas_type)
        self.oil_type = Spec("Oil Type", oil_type)

        if manual or parts_list or datasheet:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.parts_list = Spec("Parts List", Doc(parts_list))
        self.datasheet = Spec("Datasheet", Doc(datasheet))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"


# Cleaver Brooks
Burner.cb_200_100 = Burner(Make.cleaver_brooks, "CB 200 100", Fuel.natural_gas, Fuel.num_2_oil,
                           "Cleaver Brooks CB 50-100 manual.pdf", "Cleaver Brooks CB 50-100 parts list.pdf", None)
Burner.cb_200_100_150 = Burner(Make.cleaver_brooks, "CB 200 100 150", Fuel.natural_gas, Fuel.num_2_oil,
                               "Cleaver Brooks CB 50-100 manual.pdf", "Cleaver Brooks CB 50-100 parts list.pdf", None)
Burner.cble_200_150_150 = Burner(Make.cleaver_brooks, "CBLE 200 150 150", Fuel.natural_gas, Fuel.num_2_oil,
                                 "Cleaver Brooks cb-cble 125-200 manual.pdf",
                                 "Cleaver Brooks CB 125-200 parts list.pdf", None)
Burner.cble_200_150_150st = Burner(Make.cleaver_brooks, "CBLE 200 150 150ST", Fuel.natural_gas, Fuel.num_2_oil,
                                   "Cleaver Brooks cb-cble 125-200 manual.pdf",
                                   "Cleaver Brooks CB 125-200 parts list.pdf", None)

# Gordon Piatt
Burner.ks4_2_g_03 = Burner(Make.gordon_piatt, "KS4.2-G-03", Fuel.natural_gas, None,
                           "Gordon Piatt R S manual.pdf", None, "Gordon Piatt S4 data sheet.pdf")
Burner.s8_1_go_10 = Burner(Make.gordon_piatt, "S8.1-GO-10", Fuel.natural_gas, Fuel.num_2_oil,
                           "Gordon Piatt R S manual.pdf", None, None)
Burner.sr8_9_go_05 = Burner(Make.gordon_piatt, "SR8.9-GO-05", Fuel.natural_gas, Fuel.num_2_oil,
                            "Gordon Piatt R S manual.pdf", None, None)

# Power Flame
Burner.bccr2_go_20a = Burner(Make.power_flame, "BCCR2-GO-20A", Fuel.natural_gas, Fuel.num_2_oil,
                             "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)
Burner.bclnic2_go_15 = Burner(Make.power_flame, "BCCR2-GO-20A", Fuel.natural_gas, Fuel.num_2_oil,
                              "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)
Burner.c1_go_10 = Burner(Make.power_flame, "C1-GO-10", Fuel.natural_gas, Fuel.num_2_oil,
                         "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)
Burner.c2_go_15 = Burner(Make.power_flame, "C2-GO-15", Fuel.natural_gas, Fuel.num_2_oil,
                         "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)

# for var in vars(Blank):
#     print(var)
