from specifications.doc import Doc
from specifications.enums.fuel import Fuel
from specifications.enums.unit import Unit
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class GasBlockValveHead(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, volts: int or str, hertz: int or str, fuel_type: Fuel or None,
                 proof_of_closure_switch: bool, opening_time: int or None, max_closing_time: int or None, amps_opening: float or None,
                 amps_holding: float or None, manual: str or None = None, specifications: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model/Type", model)
        self.volts = Spec("Volts", volts, Unit.volt)
        self.hertz = Spec("Hz", hertz, Unit.hertz)
        self.fuel_type = Spec("Fuel Type", fuel_type)
        self.proof_of_closure_switch = Spec("Proof-of-Closure Switch", proof_of_closure_switch)
        self.opening_time = Spec("Opening Time", opening_time, Unit.second)
        self.max_closing_time = Spec("Max Closing Time", max_closing_time, Unit.second)
        self.amps_opening = Spec("Amps Opening", amps_opening, Unit.amp)
        self.amps_holding = Spec("Amps Holding", amps_holding, Unit.amp)

        # Docs
        self.manual = Spec("Manual", Doc(manual))
        self.specification = Spec("Specifications", Doc(specifications))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"


# Asco
GasBlockValveHead.ah2d112a4 = GasBlockValveHead(Make.asco, "AH2D112A4", 120, 60, Fuel.natural_gas, False, None, 1, 1.85,
                                                .11, "Asco AH2D manual.pdf")

# Honeywell
GasBlockValveHead.v4055a1098 = GasBlockValveHead(Make.honeywell, "V4055A1098", "110/120", "50/60",
                                                 Fuel.natural_gas_low_pressure, False, 13, 1, 1.57,
                                                 .13, "Honeywell V4055 A-E manual.pdf",
                                                 "Honeywell V4055 A-E specification data.pdf")
GasBlockValveHead.v4055d1019 = GasBlockValveHead(Make.honeywell, "V4055D1019", "110/120", "50/60",
                                                 Fuel.natural_gas_low_pressure, True, 13, 1, 1.57,
                                                 .13, "Honeywell V4055 A-E manual.pdf",
                                                 "Honeywell V4055 A-E specification data.pdf")
GasBlockValveHead.v4055d1076 = GasBlockValveHead(Make.honeywell, "V4055D1076", "110/120", "50/60",
                                                 Fuel.natural_gas_low_pressure, True, 13, 1, 1.57,
                                                 .13, "Honeywell V4055 A-E manual.pdf",
                                                 "Honeywell V4055 A-E specification data.pdf")

# Siemens
GasBlockValveHead.skp15_013u1 = GasBlockValveHead(Make.siemens, "SKP15.013U1", 120, 60,
                                                  None, False, None, None, None,
                                                  None, None,
                                                  "Siemens SKPx5 manual.pdf")
GasBlockValveHead.SKP25_411u1 = GasBlockValveHead(Make.siemens, "SKP25.411U1", "110/120", "50/60",
                                                  None, True, None, None, None,
                                                  None, "Siemens SKP25.xxxUx manual.pdf",
                                                  "Siemens SKPx5 manual.pdf")

# for var in vars(Blank):
#     print(var)
