from specifications.doc import Doc
from specifications.enums.item_group import ItemGroup
from specifications.enums.unit import Unit
from specifications.header import Header
from specifications.items.make import Make
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Manometer(Item):
    item_group = ItemGroup.tools

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, pressure_range: int or float, pressure_range_unit: Unit,
                 units_of_measurement: list[Unit], manual: str or None = None, datasheet: str or None = None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.pressure_range = Spec("Range", pressure_range, pressure_range_unit)
        self.units_of_measurement = Spec("Units of Measurement", units_of_measurement)

        if manual or datasheet:
            self.doc_header = Spec(None, Header("Docs"))
        self.manual = Spec("Manual", Doc(manual))
        self.datasheet = Spec("Datasheet", Doc(datasheet))


    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    def __str__(self):
        return f"{self.model} - {self.pressure_range}{self.pressure_range.unit}"


extech_hd_units_of_measurement = sorted([Unit.inches_of_water_column,
                                         Unit.pounds_per_square_inch,
                                         Unit.millibar,
                                         Unit.kilopascal,
                                         Unit.inches_of_mercury,
                                         Unit.millimeters_of_mercury,
                                         Unit.ounces_per_square_inch,
                                         Unit.feet_of_water_column,
                                         Unit.centimeter_of_water_column,
                                         Unit.kilograms_per_square_centimeter,
                                         Unit.bar])

Manometer.hd700 = Manometer(Make.extech, "HD700", 2, Unit.pounds_per_square_inch, extech_hd_units_of_measurement, "Extech HD700 manual.pdf", "Extech HD700 HD750 HD755 datasheet.pdf")
Manometer.hd750 = Manometer(Make.extech, "HD750", 5, Unit.pounds_per_square_inch, extech_hd_units_of_measurement, "Extech HD750 manual.pdf", "Extech HD700 HD750 HD755 datasheet.pdf")
Manometer.hd755 = Manometer(Make.extech, "HD755", 0.5, Unit.pounds_per_square_inch, extech_hd_units_of_measurement, "Extech HD755 manual.pdf", "Extech HD700 HD750 HD755 datasheet.pdf")

# for var in vars(Manometer):
#     print(var)
