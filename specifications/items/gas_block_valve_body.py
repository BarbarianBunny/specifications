from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.heading import Heading
from specifications.items.make import Make
from specifications.item import Item
from specifications.items.pipe_size import PipeSize
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class GasBlockValveBody(Item):
    item_group = ItemGroup.equipment

    v5055a1004 = None
    v5055a1012 = None
    v5055a1020 = None
    v5055a1038 = None
    v5055a1046 = None
    v5055a1053 = None
    v5055a1343 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, size: PipeSize or list[PipeSize], max_operating_pressure: int,
                 max_close_off: int or None, manual: str or None = None, installation: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.size = size
        self.max_operating_pressure = Spec("Max Operating Pressure", max_operating_pressure, Unit.pounds_per_square_inch)
        self.max_close_off = Spec("Max Close Off Pressure", max_close_off, Unit.pounds_per_square_inch)

        if manual or installation:
            self.doc_header = Spec(None, Heading("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.installation = Spec("Installation", Doc(installation))

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

    def __str__(self):
        if isinstance(self.size.value, list):
            return f"{self.model} - {', '.join(str(x) for x in self.size.value)}"
        else:
            return f"{self.model} - {self.size}"


# Honeywell
# V5055A
GasBlockValveBody.v5055a1004 = GasBlockValveBody(Make.honeywell, "V5055A1004", PipeSize.d1, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055a1012 = GasBlockValveBody(Make.honeywell, "V5055A1012", PipeSize.d1_25, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055a1020 = GasBlockValveBody(Make.honeywell, "V5055A1020", PipeSize.d1_5, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055a1038 = GasBlockValveBody(Make.honeywell, "V5055A1038", PipeSize.d2, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055a1046 = GasBlockValveBody(Make.honeywell, "V5055A1046", PipeSize.d2_5, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055a1053 = GasBlockValveBody(Make.honeywell, "V5055A1053", PipeSize.d3, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055a1343 = GasBlockValveBody(Make.honeywell, "V5055A1343", PipeSize.d0_75, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")

# V5055C
GasBlockValveBody.v5055c1000 = GasBlockValveBody(Make.honeywell, "V5055C1000", PipeSize.d2, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1018 = GasBlockValveBody(Make.honeywell, "V5055C1018", PipeSize.d2_5, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1026 = GasBlockValveBody(Make.honeywell, "V5055C1026", PipeSize.d3, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1034 = GasBlockValveBody(Make.honeywell, "V5055C1034", PipeSize.d1, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1042 = GasBlockValveBody(Make.honeywell, "V5055C1042", PipeSize.d1_25, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1059 = GasBlockValveBody(Make.honeywell, "V5055C1059", PipeSize.d1_5, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1109 = GasBlockValveBody(Make.honeywell, "V5055C1109", PipeSize.d4, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")
GasBlockValveBody.v5055c1182 = GasBlockValveBody(Make.honeywell, "V5055C1182", PipeSize.d0_75, 5, 15,
                                                 "Honeywell V5055 A-F manual.pdf")

# V5097
GasBlockValveBody.v5097c1018 = GasBlockValveBody(Make.honeywell, "V5097C1018",
                                                 [PipeSize.d2, PipeSize.d2_5, PipeSize.d3], 5, 15,
                                                 "Honeywell V5097 A-E manual.pdf", "Honeywell V5097 installation.pdf")

# Siemens
GasBlockValveBody.vgd20_403u = GasBlockValveBody(Make.siemens, "VGD20.403U", PipeSize.d1_5, 20, 30,
                                                 "Siemens VGDx0.xxxU manual.pdf")

# Asco
GasBlockValveBody.v710easv15 = GasBlockValveBody(Make.asco, "V710EASV15", PipeSize.d0_75, 15, None)

# for var in vars(Blank):
#     print(var)
