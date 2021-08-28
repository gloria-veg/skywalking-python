from abc import ABC, abstractmethod
from skywalking import config


# name和tag在这里要不要定义？

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
