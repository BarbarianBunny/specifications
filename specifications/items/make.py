from specifications.item import Item
from specifications.spec import Spec


class Make(Item):
    antunes = None
    asco = None
    bussmann = None
    cleveland_controls = None
    honeywell = None
    littelfuse = None
    mersen = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name: str, website: str = None):
        super().__init__()
        self.name = Spec("Name", name)
        self.website = Spec("Website", website)

    def __str__(self):
        return f"{self.name}"


Make.antunes = Make("Antunes")
Make.asco = Make("ASCO")
Make.bussmann = Make("Bussmann")
Make.cleveland_controls = Make("Cleveland Controls")
Make.honeywell = Make("Honeywell")
Make.littelfuse = Make("Littelfuse")
Make.mersen = Make("Mersen")

# for var in vars(Make):
#     print(var)
