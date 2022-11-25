from specifications.enums.unit import Unit
from specifications.item import Item


class Spec:
    def __init__(self, label: str or None, value, unit: Unit = None):
        self.label = label
        self.value = value
        self.unit = unit

    def __str__(self):
        return str(self.value)