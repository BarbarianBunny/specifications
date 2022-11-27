from specifications.doc import Doc
from specifications.enums.flame_scanner import SensorType
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.heading import Heading
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class FlameScanner(Item):
    item_group = ItemGroup.equipment

    c7027a1023 = None
    c7027a1049 = None
    c7915a1044 = None
    c7927a1016 = None
    qri2a2_b180b = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, sensor_type: SensorType, self_test: bool, manual: str = None,
                 catalogue: str = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.sensor_type = Spec("Type", sensor_type)
        self.self_test = Spec("Self Test", self_test)

        if manual or catalogue:
            self.doc_header = Spec(None, Heading("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.catalogue = Spec("Catalogue", Doc(catalogue))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"


FlameScanner.c7027a1023 = FlameScanner(Make.honeywell, "C7027A1023", SensorType.ultraviolet, False,
                                       "Honeywell C70xxA C7927A manual.pdf",
                                       "Honeywell Flame Scanner cross reference.pdf")
FlameScanner.c7027a1049 = FlameScanner(Make.honeywell, "C7027A1049", SensorType.ultraviolet, False,
                                       "Honeywell C70xxA C7927A manual.pdf",
                                       "Honeywell Flame Scanner cross reference.pdf")
FlameScanner.c7915a1044 = FlameScanner(Make.honeywell, "C7915A1044", SensorType.infrared, False,
                                       "Honeywell C7915A manual.pdf", "Honeywell Flame Scanner cross reference.pdf")
FlameScanner.c7927a1016 = FlameScanner(Make.honeywell, "C7927A1016", SensorType.ultraviolet, False,
                                       "Honeywell C70xxA C7927A manual.pdf",
                                       "Honeywell Flame Scanner cross reference.pdf")
FlameScanner.qri2a2_b180b = FlameScanner(Make.siemens, "QRI2A2.B180B", SensorType.infrared, True,
                                         "Siemens QRI2A2.B180B IR manual.pdf")

# for var in vars(Blank):
#     print(var)
