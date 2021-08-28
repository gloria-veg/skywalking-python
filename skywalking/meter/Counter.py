import BaseMeter
from enum import Enum
from skywalking.meter.BaseBuilder import BaseBuilder
import MeterId


class Mode(Enum):
    INCREMENT = 1
    RATE = 2


class Counter(BaseMeter):
    def __init__(self, meter_id: str = '', mode: str = ''):
        super(BaseMeter, self).__init__(meter_id)
        self.mode = mode

    def increment(self, count):
        pass

    def get_counter(self):
        return 0.0

    class Builder(BaseBuilder):
        def __init__(self, mode: str = '', name: str = '', meter_id=MeterId()):
            super(BaseBuilder, self).__init__(name, meter_id)
            self.mode = mode
            return self

        """override"""

        def get_meter_type(self):
            return MeterId.MeterType.COUNTER

        def create(self):
            return Counter(Counter.meter_id, Counter.mode)
