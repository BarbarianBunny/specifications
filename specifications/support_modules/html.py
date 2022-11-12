from typing import Type

from specifications.doc import Doc
from specifications.item import Item
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
    def span(cls, class_: str, contents: str) -> str:
        return f'<span class="{class_}">{contents}</span>'

    @classmethod
    def index(cls, depth=0):
        if depth == 0:
            return cls.div("index", cls.a("index.html", "index-link", "Specifications"))
        if depth == 1:
            return cls.div("index", cls.a("../index.html", "index-link", "Specifications"))

    @classmethod
    def class_html(cls, item_class: Type[Item]) -> str:
        return cls.html(
            cls.head(item_class.class_title(), 1),
            cls.body("".join([
                cls.index(1),
                cls.class_title(item_class.class_title()),
                cls.header("Items"),
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
    def docs(cls, docs: set[Doc]) -> str:
        if not docs:
            return ""
        docs_list = sorted(docs)
        return "".join([cls.header("Docs"),
                        cls.div("docs", "".join([cls.doc(doc) for doc in docs_list]))])

    @classmethod
    def doc(cls, doc: Doc) -> str:
        return cls.div("doc", cls.a(doc.href(), "doc-link", doc.title()))

    @classmethod
    def index_html(cls):
        return cls.html(
            cls.head(f'Specifications', 0),
            cls.body("".join([
                cls.index(),
                cls.header("Equipment"),
                *flatten([HTML.class_reference(subclass, 1) for subclass in Item.all_subclasses()
                          if hasattr(subclass, "items")])
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
        items = sorted(set(items))
        return cls.div("items", "".join([cls.item(item, depth) for item in items]))

    @classmethod
    def item_html(cls, item: Item):
        return cls.html(
            cls.head(f'{item.item_title()} | {item.class_title()}', 1),
            cls.body("".join([
                cls.index(1),
                cls.class_reference(item),
                cls.item_title(item.item_title()),
                cls.specs(item.specs(), item),
                cls.referrers(item)
            ])))

    @classmethod
    def item_title(cls, item_title) -> str:
        return cls.div("item-title", cls.span("item-title__text", item_title))

    @classmethod
    def specs(cls, specs, item) -> str:
        return cls.div("specs", "".join([cls.spec(spec, item) for spec in specs if isinstance(spec, Spec)]))

    @classmethod
    def spec(cls, spec: Spec, item) -> str:
        value = spec.value
        if value is None:
            return ""

        if isinstance(value, Item):
            value_contents = cls.a(f'../{value.class_kebab()}/{value.item_kebab()}.html', "item-link",
                                   value.item_title())
        elif isinstance(value, Doc):
            if value.filename is None:
                return ""
            item.docs.add(value)
            value_contents = cls.a(value.href(), "doc-link", value.title())
        else:
            value_contents = value

        if spec.unit is None:
            unit_html = ""
        else:
            unit_html = cls.span("spec__unit", spec.unit)

        spec_contents = "".join([
            cls.div("spec__label", spec.label),
            cls.span("spec__value", value_contents),
            unit_html])

        return cls.div("spec", spec_contents)

    @classmethod
    def referrers(cls, item):
        if item.referrers:
            # new version use item.referrers dict {"class title": [referrer_item, referrer_item], etc.}
            referrer_html = [cls.header("Referenced in")]
            for class_title, referrers in item.referrers.items():
                if referrers[0] is not None:
                    referrer_html.append(cls.class_reference(referrers[0], 1))
                else:
                    referrer_html.append(cls.header(class_title))
                referrers_html = []
                for referrer in sorted(referrers):
                    if referrer is not None:
                        referrers_html.append(cls.div("referrer",
                                                     cls.a(f"../{referrer.class_kebab()}/{referrer.item_kebab()}.html",
                                                           "referrer-link", referrer.item_title())))
                referrer_html.append(cls.div("referrers", "".join(referrers_html)))
            return "".join(referrer_html)
        return ""

    @classmethod
    def header(cls, text):
        return cls.div("header", cls.span("header__text", text))
