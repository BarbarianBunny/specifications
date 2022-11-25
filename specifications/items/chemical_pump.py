from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class ChemicalPump(Item):
    item_group = ItemGroup.equipment

    ewn_b11veur = None
    ezb11d1_pe = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, capacity: float, min_stroke_rate: int, max_stroke_rate: int,
                 max_psi: int, voltage: int, amp: float, manual: str = None, spec_doc: str = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.capacity = Spec("Capacity", capacity, Unit.gallon_per_hour)
        self.stroke_rate = Spec("Stroke Rate", f"{min_stroke_rate}-{max_stroke_rate}", Unit.stroke_per_minute)
        self.max_psi = Spec("Max Pressure", max_psi, Unit.pounds_per_square_inch)
        self.voltage = Spec("Voltage", voltage, Unit.volt)
        self.amp = Spec("Amp", amp, Unit.amp)

        if manual or spec_doc:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.spec_doc = Spec("Specs", Doc(spec_doc))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"


ChemicalPump.ewn_b11veur = ChemicalPump(Make.walchem, "EWN-B11VEUR", 0.6, 1, 360, 150, 115, 0.8,
                                        "Walchem EWN-R manual.pdf", "Walchem EWN-R specs.pdf")
ChemicalPump.ezb11d1_pe = ChemicalPump(Make.walchem, "EZB11D1-PE", 0.6, 1, 360, 150, 115, 0.8, "Walchem EZ manual.pdf",
                                       "Walchem EZ specs.pdf")

# for var in vars(Blank):
#     print(var)
