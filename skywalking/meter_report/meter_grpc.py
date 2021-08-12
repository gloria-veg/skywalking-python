import grpc
import random
from skywalking import config
from skywalking.protocol.language_agent import Meter_pb2
from skywalking.client import MeterReportService
from skywalking.protocol.language_agent.Meter_pb2 import MeterData
from skywalking.protocol.language_agent.Meter_pb2_grpc import MeterReportServiceStub


class GrpcMeterReportServiceClient(MeterReportServiceClient):
    def __init__(self, channel: grpc.Channel):
        self.report_stub = MeterReportServiceStub(channel)

    def report(self, generator):
        self.report_stub.collect(generator, timeout=config.GRPC_TIMEOUT)


def generate_meter(meter_list):
    print("-------------- GeneratingMeter--------------")
    for i in range(0, 5):
        random_feature = meter_list[random.randint(0, len(meter_list)-1)]
        print("Visiting point %s" % random_feature + str(i))
        yield random_feature


def run():
    with grpc.insecure_channel('localhost:11800') as channel:
        meter_list = []
        meter1 = Meter_pb2.MeterData(singleValue=Meter_pb2.MeterSingleValue(
            name='singleValueName',
            labels=[Meter_pb2.Label(
                name='LabelName1', value='LabelValue1'),
                Meter_pb2.Label(
                    name='LabelName2', value='LabelValue2')],
            value=0
        ),
            histogram=Meter_pb2.MeterHistogram(
                name='MeterHistogramName',
                labels=[Meter_pb2.Label(
                    name='LabelName1', value='LabelValue1'),
                    Meter_pb2.Label(
                        name='LabelName2', value='LabelValue2')],
                values=[]
            ),
            service='provider',
            serviceInstance='668d4b1ef83111ebbc3b8c85909c8b08',
            timestamp=0)

        meter_list.append(meter1)
        #generate_meter(meter_list)

        print("-------------- RunStart --------------")
        GrpcMeterReportServiceClient(channel).report(generate_meter(meter_list))
        print("-------------- RunEnd --------------")


if __name__ == '__main__':
    run()

    print('run ok')
