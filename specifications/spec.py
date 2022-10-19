from specifications.enums.unit import Unit


class Spec:
    def __init__(self, label: str, value=None, unit: Unit = None):
        self.label = label
        self.value = value
        self.unit = unit
