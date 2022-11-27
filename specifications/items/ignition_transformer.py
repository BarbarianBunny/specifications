from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.heading import Heading
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class IgnitionTransformer(Item):
    item_group = ItemGroup.equipment

    _1092_h = None
    _1092_pf = None
    _1092_pf_G = None
    _1092_s = None
    _1092_sg = None
    _421_655_g = None
    _421_659 = None
    _542_gp = None
    a06_sj5 = None
    a10_sj5 = None
    _312_25abo418_f92u = None
    _612_6a0202_j981 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, frame: str = None, primary_volts: int = None, hertz: int = None, volt_amps: int = None,
                 secondary_volts: int = None, milliamps: int = None, catalogue: str = None):
        super().__init__()
        self.make = make
        self.model = Spec("Catalog Number", model)
        self.frame = Spec("Frame Type", frame)
        self.primary_volts = Spec("Primary Volts", primary_volts, Unit.volt)
        self.hertz = Spec("Hertz", hertz, Unit.hertz)
        self.volt_amps = Spec("Volt Amps", volt_amps, Unit.volt_ampere)
        self.secondary_volts = Spec("Secondary Volts", secondary_volts, Unit.volt)
        self.milliamps = Spec("Milliamps", milliamps, Unit.milliamp)

        if catalogue:
            self.doc_header = Spec(None, Heading("Docs"))
        self.catalogue = Spec("Catalogue", Doc(catalogue))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        if self.frame:
            return f"{self.model} - {self.frame}"
        else:
            return f"{self.model}"


IgnitionTransformer._1092_h = IgnitionTransformer(Make.allanson, "1092", "H", 120, 60, 150, 6000, 20, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._1092_pf = IgnitionTransformer(Make.allanson, "1092", "PF", 120, 60, 150, 6000, 20, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._1092_pf_G = IgnitionTransformer(Make.allanson, "1092", "PF-G", 120, 60, 150, 6000, 20, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._1092_s = IgnitionTransformer(Make.allanson, "1092", "S", 120, 60, 150, 6000, 20, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._1092_sg = IgnitionTransformer(Make.allanson, "1092", "SG", 120, 60, 150, 6000, 20, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._421_655_g = IgnitionTransformer(Make.allanson, "421", "655 G", 120, 60, 250, 10000, 23, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._421_659 = IgnitionTransformer(Make.allanson, "421", "659", 120, 60, 250, 10000, 23, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer._542_gp = IgnitionTransformer(Make.allanson, "542", "GP", 120, 60, 265, 10000, 23, "Allanson Ignition Transformers catalogue.pdf")
IgnitionTransformer.a06_sj5 = IgnitionTransformer(Make.dongan, "A06-SJ5", None, 120, 60, 175, 6000, 20, "Dongan Ignition Transformers catalogue.pdf")
IgnitionTransformer.a10_sj5 = IgnitionTransformer(Make.dongan, "A10-SJ5", None, 120, 60, 250, 10000, 25, "Dongan Ignition Transformers catalogue.pdf")
IgnitionTransformer._312_25abo418_f92u = IgnitionTransformer(Make.webster, "312-25ABO418", "F92U", 120, 60, 2, 10000)
IgnitionTransformer._612_6a0202_j981 = IgnitionTransformer(Make.webster, "612-6A0202", "J981", 120, 60, None, 6000)



# for var in vars(Blank):
#     print(var)
