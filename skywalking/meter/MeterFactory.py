from skywalking.meter.Counter import Counter
from skywalking.meter.Gauge import Gauge
from skywalking.meter.Histogram import Histogram


class MeterFactory(object):
    """Create a counter builder by name"""

    @staticmethod
    def counter(name):
        return Counter.Builder(name)

    """Create a counter builder by meter id"""

    @staticmethod
    def counter(meter_id):
        return Counter.Builder(meter_id)

    """Create a gauge builder by name and getter"""

    @staticmethod
    def gauge(name, getter):
        return Gauge.Builder(name, getter)

    """ Create a gauge builder by meter id and getter"""

    @staticmethod
    def gauge(meter_id, getter):
        return Gauge.Builder(meter_id, getter)

    """Create a histogram builder by name"""

    @staticmethod
    def histogram(name):
        return Histogram.Builder(name)

    """Create a histogram builder by meterId"""

    @staticmethod
    def histogram(meter_id):
        return Histogram.Builder(meter_id)

