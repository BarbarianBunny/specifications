from specifications.enums.ordered_str_enum import OrderedStrEnum


class LWCOType(OrderedStrEnum):
    float = "Float"
    controller = "Controller"
    sensor = "Sensor"
    probe = "Probe"