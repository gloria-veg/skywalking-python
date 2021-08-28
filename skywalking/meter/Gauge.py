from skywalking.meter.BaseBuilder import BaseBuilder
from skywalking.meter.BaseMeter import BaseMeter
from skywalking.meter.Counter import Counter
from skywalking.meter.MeterId import MeterId


class Gauge(BaseMeter):
    """Create a counter builder by name"""

    def __init__(self, meter_id: MeterId(), getter):
        super().__init__(meter_id)

    def get(self):
        return 0.0

    class Builder(BaseBuilder):
        __getter = 0.0  # double getter

        def __init__(self, name, getter):
            super().__init__(name)
            self.__getter = getter

        def __init__(self, meter_id, getter):
            super().__init__(meter_id)
            self.__getter = getter

        """override"""

        def get_meter_type(self):
            return MeterId.MeterType.GAUGE

        def create(self):
            return Counter(Gauge.meter_id, )
