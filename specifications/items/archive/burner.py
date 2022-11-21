from specifications.doc import Doc
from specifications.enums.fuel import Fuel
from specifications.enums.unit import Unit
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Burner(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str or None, gas_type: Fuel or None,
                 gas_min_mbh: int or None, gas_max_mbh: int or None, oil_type: Fuel or None,
                 oil_min: int or None, oil_max: int or None, gas_manifold_pressure, min_circuit,
                 control_volts, control_amps, control_ph, control_hz, control_hp,
                 blower_volts, blower_amps, blower_ph, blower_hz, blower_hp,
                 air_comp_volts, air_comp_amps, air_comp_ph, air_comp_hz, air_comp_hp,
                 oil_pump_volts, oil_pump_amps, oil_pump_ph, oil_pump_hz, oil_pump_hp,
                 manual: str or None, parts_list: str or None, data_sheet: str or None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.gas_type = Spec("Gas Type", gas_type)
        self.gas_min_mbh = Spec("Gas min", gas_min_mbh, Unit.thousand_btu_per_hour)
        self.gas_max_mbh = Spec("Gas max", gas_max_mbh, Unit.thousand_btu_per_hour)
        self.oil_type = Spec("Oil Type", oil_type)
        self.oil_min = Spec("Oil min", oil_min, Unit.gallon_per_hour)
        self.oil_max = Spec("Oil max", oil_max, Unit.gallon_per_hour)
        self.gas_manifold = Spec("Gas Manifold", gas_manifold_pressure, Unit.inches_of_water_column)

        self.min_circuit = Spec("Min Circuit Amps", min_circuit, Unit.amp)
        self.control_volts = Spec("Control Volts", control_volts, Unit.volt)
        self.control_amps = Spec("Control Amps", control_amps, Unit.amp)
        self.control_ph = Spec("Control PH", control_ph, Unit.phase)
        self.control_hz = Spec("Control Hz", control_hz, Unit.hertz)
        self.control_hp = Spec("Control HP", control_hp, Unit.horse_power)

        self.blower_volts = Spec("Blower Volts", blower_volts, Unit.volt)
        self.blower_amps = Spec("Blower Amps", blower_amps, Unit.amp)
        self.blower_ph = Spec("Blower PH", blower_ph, Unit.phase)
        self.blower_hz = Spec("Blower Hz", blower_hz, Unit.hertz)
        self.blower_hp = Spec("Blower HP", blower_hp, Unit.horse_power)

        self.air_comp_volts = Spec("Air Comp Volts", air_comp_volts, Unit.volt)
        self.air_comp_amps = Spec("Air Comp Amps", air_comp_amps, Unit.amp)
        self.air_comp_ph = Spec("Air Comp PH", air_comp_ph, Unit.phase)
        self.air_comp_hz = Spec("Air Comp Hz", air_comp_hz, Unit.hertz)
        self.air_comp_hp = Spec("Air Comp HP", air_comp_hp, Unit.horse_power)

        self.oil_pump_volts = Spec("Oil Pump Volts", oil_pump_volts, Unit.volt)
        self.oil_pump_amps = Spec("Oil Pump Amps", oil_pump_amps, Unit.amp)
        self.oil_pump_ph = Spec("Oil Pump PH", oil_pump_ph, Unit.phase)
        self.oil_pump_hz = Spec("Oil Pump Hz", oil_pump_hz, Unit.hertz)
        self.oil_pump_hp = Spec("Oil Pump HP", oil_pump_hp, Unit.horse_power)

        self.manual = Spec("Manual", Doc(manual))
        self.parts_list = Spec("Parts List", Doc(parts_list))
        self.data_sheet = Spec("Data Sheet", Doc(data_sheet))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"


# Cleaver Brooks
Burner.cb_200_100 = Burner(Make.cleaver_brooks, "CB 200 100", Fuel.natural_gas, None, 4185, Fuel.num_2_oil, None, 30, None,
                           23.5, 120, 7, 1, 60, None,
                           230, 20.7, 3, 60, 3,
                           None, None, None, None, None,
                           230, 1.3, 1, 60, None,
                           "Cleaver Brooks CB 50-100 manual.pdf", "Cleaver Brooks CB 50-100 parts list.pdf", None)
Burner.cb_200_100_150 = Burner(Make.cleaver_brooks, "CB 200 100 150", Fuel.natural_gas, None, 4185, Fuel.num_2_oil, None, 30, None,
                               26.5, 120, 7, 1, 60, None,
                               208, 21, 3, 60, 3,
                               None, None, None, None, None,
                               208, 2.3, 3, 60, None,
                               "Cleaver Brooks CB 50-100 manual.pdf", "Cleaver Brooks CB 50-100 parts list.pdf", None)
Burner.cble_200_150_150 = Burner(Make.cleaver_brooks, "CBLE 200 150 150", Fuel.natural_gas, None, 6124, Fuel.num_2_oil, None, 43.7, 4.4,
                                 48, 120, 7, 1, 60, None,
                                 None, 2.1, None, None, 7.5,
                                 None, None, None, None, 3,
                                 208, 2.5, 3, 60, None,
                                 "Cleaver Brooks cb-cble 125-200 manual.pdf", "Cleaver Brooks CB 125-200 parts list.pdf", None)
Burner.cble_200_150_150st = Burner(Make.cleaver_brooks, "CBLE 200 150 150ST", Fuel.natural_gas, 1531, 6124, Fuel.num_2_oil, 10.9, 43.7, 4.4,
                                 20, 120, 7, 1, 60, None,
                                 None, 9, None, None, 7.5,
                                 None, None, None, None, 3,
                                 115, 9.8, 1, 60, None,
                                 "Cleaver Brooks cb-cble 125-200 manual.pdf", "Cleaver Brooks CB 125-200 parts list.pdf", None)

# Gordon Piatt
Burner.ks4_2_g_03 = Burner(Make.gordon_piatt, "KS4.2-G-03", Fuel.natural_gas, None, None, None, None, None, None,
                           None, None, None, None, None, None,
                           None, None, None, None, None,
                           None, None, None, None, None,
                           None, None, None, None, None,
                           "Gordon Piatt R S manual.pdf", None, "Gordon Piatt S4 data sheet.pdf")
Burner.s8_1_go_10 = Burner(Make.gordon_piatt, "S8.1-GO-10", Fuel.natural_gas, 1260, 2100, Fuel.num_2_oil, 9, 15, "1.2 - 3.37",
                           None, 120, 5, 1, 60, 1,
                           120, 12, 1, 60, "1/3",
                           None, None, None, None, None,
                           120, 7, 1, 60, None,
                           "Gordon Piatt R S manual.pdf", None, None)
Burner.sr8_9_go_05 = Burner(Make.gordon_piatt, "SR8.9-GO-05", Fuel.natural_gas, 500, 1500, Fuel.num_2_oil, 3.6, 10.7, "0.5 - 3.3",
                           None, 120, 5, 1, 60, "1/2",
                           120, 7.4, 1, 60, None,
                           None, None, None, None, None,
                            None, None, None, None, None,
                           "Gordon Piatt R S manual.pdf", None, None)

# Power Flame
Burner.bccr2_go_20a = Burner(Make.power_flame, "BCCR2-GO-20A", Fuel.natural_gas, 750, 2319, Fuel.num_2_oil, 5.5, 16.6, 2.5,
                           17.9, 115, 6, 1, 60, None,
                           115, 9.8, 1, 60, "3/4",
                           None, None, None, None, None,
                           115, 5.6, 1, 60, "1/3",
                           "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)
Burner.bclnic2_go_15 = Burner(Make.power_flame, "BCCR2-GO-20A", Fuel.natural_gas, 750, 1674, Fuel.num_2_oil, 5.5, 12, 1.7,
                             12.2, 115, 6, 1, 60, None,
                             230, 4.8, 1, 60, "3/4",
                             None, None, None, None, None,
                             230, 2.7, 1, 60, "1/3",
                             "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)
Burner.c1_go_10 = Burner(Make.power_flame, "C1-GO-10", Fuel.natural_gas, 300, 924, Fuel.num_2_oil, 2.5, 6.6, 2.2,
                             18.25, 115, 6, 1, 60, None,
                             115, 7.4, 1, 60, "1/2",
                             None, None, None, None, None,
                             115, 5.6, 1, 60, "1/3",
                             "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)
Burner.c2_go_15 = Burner(Make.power_flame, "C2-GO-15", Fuel.natural_gas, 750, 1633, Fuel.num_2_oil, 5.5, 11.7, 1.9,
                         17.9, 115, 6, 1, 60, None,
                         208, 4.8, 1, 60, "3/4",
                         None, None, None, None, None,
                         208, 3.5, 1, 60, "1/2",
                         "Power Flame C manual.pdf", "Power Flame C parts list.pdf", None)


# for var in vars(Blank):
#     print(var)
