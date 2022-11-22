from typing import Type

from specifications.doc import Doc
from specifications.item import Item
from specifications.link import Link
from specifications.spec import Spec
from specifications.support_modules.flatten_list import flatten


class HTML:

    @classmethod
    def a(cls, href, contents: str, class_: str = "link") -> str:
        return f'<a href="{href}" class="{class_}">{contents}</a>'

    @classmethod
    def body(cls, contents: str) -> str:
        return f'<body>{contents}</body>'

    @classmethod
    def div(cls, class_: str, contents: str) -> str:
        return f'<div class="{class_}">{contents}</div>'

    @classmethod
    def head(cls, title: str, depth=0) -> str:
        meta = '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        css = ''
        if depth == 0:
            css = '<link rel="stylesheet" href="styles.css"/>'
        elif depth == 1:
            css = '<link rel="stylesheet" href="../styles.css"/>'
        favicon = ''
        return f'{meta}{css}<title>{title}</title>{favicon}'

    @classmethod
    def html(cls, head, body) -> str:
        return f'<!DOCTYPE html><html lang="end">{head}{body}</html>'

    @classmethod
    def span(cls, contents: str, class_: str = "text") -> str:
        return f'<span class="{class_}">{contents}</span>'

    @classmethod
    def index(cls, depth=0):
        if depth == 0:
            return cls.div("index", cls.a("index.html", "Specifications"))
        if depth == 1:
            return cls.div("index", cls.a("../index.html", "Specifications"))

    @classmethod
    def class_html(cls, item_class: Type[Item]) -> str:
        return cls.html(
            cls.head(item_class.class_title(), 1),
            cls.body("".join([
                cls.index(1),
                cls.header(cls.span(item_class.class_title())),
                cls.items(item_class.items),
                cls.docs(item_class.docs)
            ])))

    @classmethod
    def class_link(cls, item, depth: int = 0) -> str:
        if depth == 0:
            return cls.a(f'{item.class_kebab()}.html', item.class_title())
        elif depth == 1:
            return cls.a(f'{item.class_kebab()}/{item.class_kebab()}.html', item.class_title())
        elif depth == 2:
            return cls.a(f'../{item.class_kebab()}/{item.class_kebab()}.html', item.class_title())

    @classmethod
    def docs(cls, docs: set[Doc]) -> str:
        if not docs:
            return ""
        docs_list = sorted(docs)
        return "".join([cls.header(cls.span("Docs")),
                        cls.div("docs", "".join([cls.doc(doc) for doc in docs_list]))])

    @classmethod
    def doc(cls, doc: Doc) -> str:
        return cls.div("item", cls.a(doc.href(), doc.title()))

    @classmethod
    def index_html(cls):
        return cls.html(
            cls.head(f'Specifications', 0),
            cls.body("".join([
                cls.index(),
                cls.index_item_subclasses()
            ])))

    @classmethod
    def index_item_subclasses(cls) -> str:
        subclass_html = []
        subclasses_by_group = {}
        for subclass in Item.all_subclasses():
            if hasattr(subclass, "items") and hasattr(subclass, "item_group"):
                if subclass.item_group in subclasses_by_group:
                    subclasses_by_group[subclass.item_group].append(cls.div("item", cls.class_link(subclass, 1)))
                else:
                    subclasses_by_group[subclass.item_group] = [cls.div("item", cls.class_link(subclass, 1))]

        for item_group, items in subclasses_by_group.items():
            subclass_html.append(cls.header(cls.span(item_group)))
            subclass_html.append(cls.div("group", "".join(items)))

        return "".join(subclass_html)

    @classmethod
    def item(cls, item: Item, depth: int = 0):
        if depth == 0:
            return cls.div("item", cls.a(f'{item.item_kebab()}.html', item.item_title()))
        elif depth == 1:
            return cls.div("item",
                           cls.a(f'{item.class_kebab()}/{item.item_kebab()}.html', item.item_title()))

    @classmethod
    def items(cls, items, depth: int = 0):
        items = sorted(set(items))
        return cls.div("items", "".join([cls.item(item, depth) for item in items]))

    @classmethod
    def item_html(cls, item: Item):
        return cls.html(
            cls.head(f'{item.item_title()} | {item.class_title()}', 1),
            cls.body("".join([
                cls.index(1),
                cls.header(cls.class_link(item)),
                cls.header(cls.span(item.item_title())),
                cls.specs(item.specs(), item),
                cls.referrers(item)
            ])))

    @classmethod
    def item_title(cls, item_title) -> str:
        return cls.div("item-title", cls.span(item_title))

    @classmethod
    def specs(cls, specs, item) -> str:
        return cls.div("specs", "".join([cls.spec(spec, item) for spec in specs if isinstance(spec, Spec)]))

    @classmethod
    def spec(cls, spec: Spec, item) -> str:
        value = spec.value
        if value is None:
            return ""

        value_contents = cls.spec_value(item, value, spec.unit)
        if value_contents is None:
            return ""

        spec_contents = "".join([
            cls.div("spec__label", spec.label),
            value_contents])

        return cls.div("spec", spec_contents)

    @classmethod
    def spec_unit(cls, unit):
        if unit is None:
            return ""
        else:
            return cls.span(unit)

    @classmethod
    def spec_value(cls, item, value, unit):
        if isinstance(value, list):
            values = []
            for thing in value:
                values.append(cls.spec_value(item, thing, unit))
            return ", ".join(values)
        elif isinstance(value, Item):
            return cls.a(f'../{value.class_kebab()}/{value.item_kebab()}.html', value.item_title()) + cls.spec_unit(
                unit)
        elif isinstance(value, Doc):
            if value.filename is None:
                return None
            item.docs.add(value)
            return cls.a(value.href(), value.title())
        elif isinstance(value, Link):
            if value.url is None:
                return ""
            return cls.a(value.url, value.url)
        else:
            return cls.span(value) + cls.spec_unit(unit)

    @classmethod
    def referrers(cls, item):
        if item.referrers:
            # new version use item.referrers dict {"class title": [referrer_item, referrer_item], etc.}
            referrer_html = [cls.header(cls.span("Referenced in"))]
            for class_title, referrers in item.referrers.items():
                if referrers[0] is not None:
                    referrer_html.append(cls.header(cls.class_link(referrers[0], 2)))
                else:
                    referrer_html.append(cls.header(cls.span(class_title)))
                referrers_html = []
                for referrer in sorted(referrers):
                    if referrer is not None:
                        referrers_html.append(
                            cls.div("item",
                                    cls.a(f"../{referrer.class_kebab()}/{referrer.item_kebab()}.html",
                                          referrer.item_title())))
                referrer_html.append(cls.div("referrers", "".join(referrers_html)))
            return "".join(referrer_html)
        return ""

    @classmethod
    def header(cls, content):
        return cls.div("header", content)
