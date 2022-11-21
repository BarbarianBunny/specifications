from specifications.item import Item


class item_property(property):
    # update the property's value's referrers with the instance

    def __set__(self, instance, value):
        if isinstance(value, Item):
            value.referrers.setdefault(instance.class_title(), []).append(instance)
        super().__set__(instance, value)
