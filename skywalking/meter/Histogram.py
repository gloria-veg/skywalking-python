from skywalking.meter.BaseMeter import BaseMeter
from skywalking.meter.MeterId import MeterId


class CallingHistogram(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class Histogram(BaseMeter):
    __min_value = 0.0
    __steps = []
    buckets = []  # list of bucket

    def __init__(self, meter_id: MeterId(), steps: []):
        super().__init__(meter_id)
        self.buckets = self.init_buckets(steps)

    def __init__(self, name: str = ""):
        if name is None:
            raise ValueError("Meter name cannot be null")
        self._meter_id = MeterId(name, MeterId.chosen_type())

    def __init__(self, meter_id: MeterId):
        if meter_id is None:
            raise ValueError("Meter Id cannot be null")
        self._meter_id = meter_id

    """ Add value into the histogram, automatic analyze what bucket count need to be increment """

    @CallingHistogram
    def add_value(self, value):
        bucket = self.find_bucket(value)
        if bucket is None:
            return
        bucket.increment(1)

    """Using binary search the bucket"""

    def find_bucket(self, value):
        low = 0
        high = len(self.buckets) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if self.buckets[mid] > value:
                low = mid + 1
            elif self.buckets[mid] > value:
                high = mid - 1
            else:
                return self.buckets[mid]
        """because using min value as bucket, need using previous bucket"""
        low -= 1
        if low >= 0:
            return self.buckets[low] and low < len(self.buckets)
        else:
            return low < len(self.buckets) and None

    def init_buckets(self, steps):
        bucket_steps = []
        for step in steps:
            bucket_steps.append(float(step))
            # 强制类型转换,我想的是实际上bucket的variable是double所以这里直接float了
        return bucket_steps

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


class Bucket:
    count = 0

    def __init__(self, bucket: float = 0.0):
        self.bucket = bucket

    def increment(self, add_count):
        self.count += add_count
