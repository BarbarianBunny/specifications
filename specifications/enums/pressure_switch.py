from specifications.enums.ordered_str_enum import OrderedStrEnum


class BreaksOn(OrderedStrEnum):
    fall = "Fall"  # Low Pressure Switch
    rise = "Rise"  # High Pressure Switch


class ResetType(OrderedStrEnum):
    auto = "Auto"
    manual = "Manual"