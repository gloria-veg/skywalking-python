import BaseMeter
from enum import Enum
import MeterId


class Mode(Enum):
    INCREMENT = 1
    RATE = 2


class CallingCounter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class Counter(BaseMeter):
    def __init__(self, meter_id: str = '', mode: str = '', name: str = ''):
        super(BaseMeter, self).__init__(meter_id, name)
        self.mode = mode
        self.name = name

    @CallingCounter
    def increment(self, count):
        pass

    def get_counter(self):
        return 0.0

    """override"""

    def get_meter_type(self):
        return MeterId.MeterType.COUNTER

    def create(self):
        return Counter(Counter.meter_id, Counter.mode, Counter.name)
