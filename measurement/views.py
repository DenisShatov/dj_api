from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer
from measurement.models import Sensor


class SensorView(CreateAPIView, ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def create_sensor(self, request):
        request.save()


class UpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def update_sensor(self, request):
        request.save()


class AddMeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def update_measurement(self, request):
        request.save()
