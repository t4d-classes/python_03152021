import json
import yaml


class JsonMixin:

    def to_json(self):
        return json.dumps(self._items)


class YamlMixin:

    def to_yaml(self):
        return yaml.dump(self._items)


class Parent:

    def __init__(self):
        self._items = []


class Child(Parent, JsonMixin, YamlMixin):

    def __init__(self):
        super().__init__()

    def append(self, name, age):
        self._items.append({"name": name, "age": age})

    def __iter__(self):
        return iter(self._items)

    def __next__(self):
        return next(self._items)


child = Child()
child.append("Bob", 23)
child.append("Sally", 21)

print(child.to_json())
print(child.to_yaml())
