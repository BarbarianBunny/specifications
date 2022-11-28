from urllib.parse import quote
from weakref import WeakSet

from specifications.enums.item_group import ItemGroup
from specifications.support_modules.convert_case import ConvertCase


class Item:
    def __init__(self):
        self.referrers = {}

    def __new__(cls, *args, **kwargs):
        item = object.__new__(cls, *args, **kwargs)
        if "items" not in cls.__dict__:
            cls.items = set()  # WeakSet
        cls.items.add(item)
        if "docs" not in cls.__dict__:
            cls.docs = set()
        if "item_group" not in cls.__dict__:
            cls.item_group = ItemGroup.equipment
        return item

    def __lt__(self, other):
        return self.__str__() < other.__str__()

    def __str__(self):
        # Override in Subclass
        return f""

    @classmethod
    def class_title(cls):
        return ConvertCase.pascal_to_title(cls.__name__)

    @classmethod
    def class_kebab(cls):
        return ConvertCase.pascal_to_kebab(cls.__name__)

    @classmethod
    def all_subclasses(cls):
        return sorted(set(cls.__subclasses__()).union([subclass for c in cls.__subclasses__() for subclass in c.all_subclasses()]), key=lambda subclass: subclass.__name__)

    def item_title(self):
        return self.__str__()

    def item_kebab(self):
        return ConvertCase.kebab_case(self.__str__())

    def safe_item_kebab(self):
        return quote(self.item_kebab(), safe="%")

    def specs(self):
        return vars(self).values()
