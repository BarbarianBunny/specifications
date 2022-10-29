from specifications.item import Item


class item_property(property):

    def __set__(self, instance, value):
        if isinstance(value, Item):
            value.referrers.setdefault(instance.class_title(), []).append(instance)
        super().__set__(instance, value)
