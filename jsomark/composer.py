from json import loads
from lxml.etree import Element


class Composer:
    def __init__(self, namespaces=None):
        self.namespaces = namespaces

    def compose(self, obj):
        """Compose XML element from obj dict."""
        if isinstance(obj, (str, bytes)):
            obj = loads(obj)
        tag, content = next(iter(obj.items()))
        return self._build(self._make_element(tag), content)

    def _build(self, parent, item):
        """Recursively build XML element from item object."""
        if isinstance(item, (int, float)):
            item = str(item)
        if isinstance(item, str):
            parent.text = item
            return parent

        elif isinstance(item, dict):
            text = item.pop("#", None)
            if text is not None:
                parent.text = text

            attributes = item.pop("&", {})
            for attribute, value in attributes.items():
                parent.set(attribute, value)

            for tag, content in item.items():
                if not isinstance(content, (list, tuple)):
                    content = [content]
                for line in content:
                    element = self._make_element(tag)
                    parent.append(self._build(element, line))

        return parent

    def _make_element(self, tag):
        if self.namespaces and ':' in tag:
            prefix, name = tag.split(':')
            tag = "{{{namespace}}}{name}".format(
                namespace=self.namespaces[prefix], name=name)

        return Element(tag, nsmap=self.namespaces)
