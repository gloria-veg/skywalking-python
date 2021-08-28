from skywalking.meter.BaseBuilder import BaseBuilder
from skywalking.meter.BaseMeter import BaseMeter
from skywalking.meter.MeterId import MeterId


class Histogram(BaseMeter):
    def __init__(self, meter_id: MeterId(), steps: []):
        super().__init__(meter_id)
        self.steps = steps

    """ Add value into the histogram, automatic analyze what bucket count need to be increment """

    def add_value(self, value):
        pass

    class Builder(BaseBuilder):
        __min_value = 0.0
        __steps = []

        def __init__(self, name: str = ""):
            super(BaseBuilder, self).__init__(name)

        def __init__(self, meter_id: MeterId):
            super(BaseBuilder, self).__init__(meter_id)

        """Set bucket steps, the minimal values of every buckets besides the {@link #minValue}."""

        @property
        def steps(self):
            return self.__steps

        @steps.setter
        def steps(self, steps):
            self.steps = steps

        @property
        def min_value(self):
            return self.__steps

        @min_value.setter
        def min_value(self, min_value):
            self.min_value = min_value

        """override"""

        def get_meter_type(self):
            return MeterId.MeterType.COUNTER

        def create(self):
            if self.steps is None or self.steps == []:
                return ValueError("Missing steps setting")

            steps = sorted(self.steps)
            if steps[0] < self.min_value:
                return ValueError("Step[0] must be  bigger than min value")
            elif steps[0] != self.min_value:
                steps.insert(0, self.min_value)

            return Histogram(self.meter_id, steps)
