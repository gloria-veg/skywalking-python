from skywalking.meter.BaseMeter import BaseMeter
import MeterId


class Gauge(BaseMeter):
    """Create a counter builder by name"""

    def __init__(self, meter_id: MeterId(), getter):
        super().__init__(meter_id)
        self.getter = getter

    def __init__(self, name, getter):
        super().__init__(name)
        self.getter = getter

    def get_gauge(self):
        return 0.0

    """override"""

    def get_meter_type(self):
        return MeterId.MeterType.GAUGE

    def create(self):
        return Gauge(self.meter_id, self.getter)
