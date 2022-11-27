from specifications.enums.ordered_str_enum import OrderedStrEnum


class Issue(OrderedStrEnum):
    bug = "Bug"
    information = "Information"
    correction = "Correction"
    feature = "Feature"
