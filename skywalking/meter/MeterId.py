import functools
from enum import Enum


class MeterType(Enum):
    COUNTER = 1
    GAUGE = 2
    HISTOGRAM = 3


@functools.total_ordering
class Tag(object):
    def __init__(self, name: str = '', value: str = ''):
        self.__name = name
        self.__value = value  # type: str

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __lt__(self, other):
        if self.name == other.name:
            return self.value < other.value
        return self.name < other.value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value


class MeterId(object):
    _tags = []
    _name = ''
    _chosen_type = MeterType()

    def __init__(self, name: str, chosen_type: MeterType):
        self._name = name
        self._chosen_type = chosen_type

    def __init__(self, name: str, chosen_type: MeterType, tags):
        self._name = name
        self._chosen_type = chosen_type
        self._tags = tags.extend(tags)

    @property
    def name(self):
        return self._name

    @property
    def chosen_type(self):
        return self._chosen_type

    @property
    def tags(self):
        return self._tags

    def copy_to(self, name, chosen_type):
        return MeterId(name, chosen_type, self.tags)  #tags能这样写吗

    def __eq__(self, other):
        """Overrides the default implementation"""
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))
