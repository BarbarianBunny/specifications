from typing import Type

from specifications.doc import Doc
from specifications.item import Item
from specifications.items.plant import Plant
from specifications.spec import Spec
from specifications.support_modules.flatten_list import flatten


class HTML:

    @classmethod
    def a(cls, href, class_: str, contents: str) -> str:
        return f'<a href="{href}" class="{class_}">{contents}</a>'

    @classmethod
    def body(cls, contents: str) -> str:
        return f'<body>{contents}</body>'

    @classmethod
    def div(cls, class_: str, contents: str) -> str:
        return f'<div class="{class_}">{contents}</div>'

    @classmethod
    def head(cls, title: str) -> str:
        meta = ''
        css = ''
        favicon = ''
        return f'{meta}{css}<title>{title}</title>{favicon}'

    @classmethod
    def html(cls, head, body) -> str:
        return f'<!DOCTYPE html><html lang="end">{head}{body}</html>'

    @classmethod
    def span(cls, class_: str, contents: str) -> str:
        return f'<span class="{class_}">{contents}</span>'

    @classmethod
    def index(cls, depth=0):
        if depth == 0:
            return cls.div("index", cls.a("index.html", "index-link", "JBLM Steam"))
        if depth == 1:
            return cls.div("index", cls.a("../index.html", "index-link", "JBLM Steam"))

    @classmethod
    def class_html(cls, item_class: Type[Item]) -> str:
        return cls.html(
            cls.head(item_class.class_title()),
            cls.body("".join([
                cls.index(1),
                cls.class_title(item_class.class_title()),
                cls.div("header", cls.span("header__text", "Items")),
                cls.items(item_class.items),
                cls.docs(item_class.docs)
            ])))

    @classmethod
    def class_reference(cls, item, depth: int = 0) -> str:
        if depth == 0:
            return cls.div("class-ref", cls.a(f'{item.class_kebab()}.html', "class-ref__link", item.class_title()))
        elif depth == 1:
            return cls.div("class-ref", cls.a(f'{item.class_kebab()}/{item.class_kebab()}.html', "class-ref__link",
                                              item.class_title()))

    @classmethod
    def class_title(cls, class_title) -> str:
        return cls.div("class-title", cls.span("class-title__text", class_title))

    @classmethod
    def docs(cls, docs: list[Doc]) -> str:
        if not docs:
            return ""
        docs.sort()
        return "".join([cls.div("header", cls.span("header__text", "Docs")),
                        cls.div("docs", "".join([cls.doc(doc) for doc in docs]))])

    @classmethod
    def doc(cls, doc: Doc) -> str:
        return cls.div("doc", cls.a(doc.href(), "doc-link", doc.title()))

    @classmethod
    def index_html(cls):
        return cls.html(
            cls.head(f'JBLM Steam'),
            cls.body("".join([
                cls.index(),
                cls.div("header", cls.span("header__text", "Plants")),
                cls.items(Plant.items, 1),
                cls.div("header", cls.span("header__text", "Equipment")),
                *flatten([HTML.class_reference(subclass, 1) for subclass in Item.__subclasses__()
                          if subclass is not Plant and hasattr(subclass, "items")])
            ])))

    @classmethod
    def item(cls, item: Item, depth: int = 0):
        if depth == 0:
            return cls.div("item", cls.a(f'{item.item_kebab()}.html', "item-link", item.item_title()))
        elif depth == 1:
            return cls.div("item",
                           cls.a(f'{item.class_kebab()}/{item.item_kebab()}.html', "item-link", item.item_title()))

    @classmethod
    def items(cls, items, depth: int = 0):
        items = sorted(list(items))
        return cls.div("items", "".join([cls.item(item, depth) for item in items]))

    @classmethod
    def item_html(cls, item: Item):
        return cls.html(
            cls.head(f'{item.item_title()} | {item.class_title()}'),
            cls.body("".join([
                cls.index(1),
                cls.class_reference(item),
                cls.item_title(item.item_title()),
                cls.specs(item.specs(), item)
            ])))

    @classmethod
    def item_title(cls, item_title) -> str:
        return cls.div("item-title", cls.span("item-title__text", item_title))

    @classmethod
    def specs(cls, specs, item) -> str:
        return cls.div("specs", "".join([cls.spec(spec, item) for spec in specs]))

    @classmethod
    def spec(cls, spec: Spec, item) -> str:
        value = spec.value
        if value is None:
            return ""

        if isinstance(value, Item):
            value_contents = cls.a(f'../{value.class_kebab()}/{value.item_kebab()}.html', "item-link",
                                   value.item_title())
        elif isinstance(value, Doc):
            item.docs.append(value)
            value_contents = cls.a(value.href(), "doc-link", value.title())
        else:
            value_contents = value

        if spec.unit is None:
            unit_html = ""
        else:
            unit_html = cls.div("spec__unit", spec.unit)

        spec_contents = "".join([
            cls.span("spec__label", spec.label),
            cls.span("spec__value", value_contents),
            unit_html])

        return cls.div("spec", spec_contents)
