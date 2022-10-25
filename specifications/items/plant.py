from specifications.enums.building import Building
from specifications.item import Item
from specifications.spec import Spec


class Plant(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, building: Building):
        super().__init__()
        self.building = Spec("Building", building)

    def __str__(self):
        return f"{self.building}"


Plant.plant_1163 = Plant(Building.bldg_1163)

Plant.plant_2004 = Plant(Building.bldg_2004)

Plant.plant_2022 = Plant(Building.bldg_2022)

Plant.plant_2026 = Plant(Building.bldg_2026)

Plant.plant_2027 = Plant(Building.bldg_2027)

Plant.plant_2054 = Plant(Building.bldg_2054)

Plant.plant_2162 = Plant(Building.bldg_2162)

Plant.plant_3757 = Plant(Building.bldg_3757)

Plant.plant_3910 = Plant(Building.bldg_3910)

Plant.plant_4043 = Plant(Building.bldg_4043)

Plant.plant_9576 = Plant(Building.bldg_9576)

Plant.plant_9580 = Plant(Building.bldg_9580)

Plant.plant_9620 = Plant(Building.bldg_9620)

Plant.plant_9665 = Plant(Building.bldg_9665)

Plant.plant_9669 = Plant(Building.bldg_9669)

Plant.plant_9785 = Plant(Building.bldg_9785)

Plant.plant_9996 = Plant(Building.bldg_9996)

Plant.plant_A0310 = Plant(Building.bldg_A0310)

Plant.plant_J00734 = Plant(Building.bldg_J00734)

Plant.plant_J00853 = Plant(Building.bldg_J00853)
