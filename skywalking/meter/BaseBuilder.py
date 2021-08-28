from abc import ABC, abstractmethod
import BaseMeter
from skywalking.meter.MeterId import MeterId
from skywalking.meter.MeterId import Tag


class BaseBuilder(ABC):
    """Build a new meter build, meter name is required """

    def __init__(self, name):
        super(BaseMeter).__init__()
        if name is None:
            raise ValueError("Meter name cannot be null")
        self._meter_id = MeterId(name, MeterId.chosen_type())

    """Build a new meter build from exists meter id"""

    def __init__(self, meter_id: MeterId()):
        super(BaseMeter).__init__()
        if meter_id is None:
            raise ValueError("Meter Id cannot be null")
        self._meter_id = meter_id

    """Get supported build meter type"""

    @abstractmethod
    def get_meter_type(self):
        return MeterId.chosen_type

    '''create a meter'''

    @abstractmethod
    def create(self):
        return

    """ append new tags to this meter"""

    def get_tag(self, name, value):
        MeterId.tags().add(Tag(name, value))
        return #这里这个(builder)this 怎么return

    def build(self):
        self._meter_id.tags() #还要sort一下？
        """create or get the meter"""
        return BaseBuilder.create()
