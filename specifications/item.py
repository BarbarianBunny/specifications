from weakref import WeakSet

from specifications.support_modules.convert_case import ConvertCase


class Item:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        item = object.__new__(cls, *args, **kwargs)
        if "items" not in cls.__dict__:
            cls.items = WeakSet()
        cls.items.add(item)
        if "docs" not in cls.__dict__:
            cls.docs = list()
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

    def item_title(self):
        return self.__str__()

    def item_kebab(self):
        return ConvertCase.kebab_case(self.__str__())

    def specs(self):
        return vars(self).values()
