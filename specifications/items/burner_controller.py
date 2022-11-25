from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class BurnerController(Item):
    item_group = ItemGroup.equipment

    mii_mc120 = None
    r7140l1009 = None
    rm7800g1018 = None
    rm7800l1012 = None
    rm7800l1087 = None
    rm7800l1095 = None
    rm7840l1018 = None
    rm7895c1012 = None
    lmv52_240b1 = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, manual: str = None, codes: str = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)

        if manual or codes:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.codes = Spec("Codes", Doc(codes))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model}"


BurnerController.mii_mc120 = BurnerController(Make.fireye, "MII MC120", "Fireye M II manual.pdf")
BurnerController.r7140l1009 = BurnerController(Make.honeywell, "R7140L1009", "Honeywell R7140x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.rm7800g1018 = BurnerController(Make.honeywell, "RM7800G1018", "Honeywell RM7800x RM7840x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.rm7800l1012 = BurnerController(Make.honeywell, "RM7800L1012", "Honeywell RM7800x RM7840x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.rm7800l1087 = BurnerController(Make.honeywell, "RM7800L1087", "Honeywell RM7800x RM7840x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.rm7800l1095 = BurnerController(Make.honeywell, "RM7800L1095", "Honeywell RM7800x RM7840x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.rm7840l1018 = BurnerController(Make.honeywell, "RM7840L1018", "Honeywell RM7800x RM7840x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.rm7895c1012 = BurnerController(Make.honeywell, "RM7895C1012", "Honeywell RM7895x manual.pdf", "Honeywell S7800A display fault codes.pdf")
BurnerController.lmv52_240b1 = BurnerController(Make.honeywell, "LMV52.240B1", "Siemens LMV5 manual.pdf")


# for var in vars(Blank):
#     print(var)
