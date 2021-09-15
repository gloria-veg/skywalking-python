from abc import ABC, abstractmethod
from enum import Enum


class BaseMeter(ABC):
    @abstractmethod
    def __init__(self, meter_id: str = '', name: str = '', tag: str = ''):
        self.meter_id = meter_id
        self.name = name
        self.tag = tag

    @property
    def meter_id(self):
        return None

    @property
    def name(self):
        return ""

    @property
    def tag(self):
        return ""

    class MeterType(Enum):
        COUNTER = 1
        GAUGE = 2
        HISTOGRAM = 3

    def get_meter_type(self):
        return None


