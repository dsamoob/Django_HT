
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDescriptionSerializer, MeasurementSerializer, SensorUpdateSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDescriptionSerializer

class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer

#
#
# class SensorView(APIView):
#     def get(self, request, pk=None):
#         sensor = Sensor.objects.filter(pk=pk)
#         ser = SensorSerializer(sensor)
#         values = Measurement.objects.filter(id_sensor=pk).all()
#         values_serial = MeasurementSerializer(values, many=True)
#         return Response({'sensor': ser.data, 'measurements': values_serial.data})
#
#
#
#     def post(self, request):
#         serializer = SensorSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# class SensorViews(RetrieveAPIView):
#     queryset = Sensor.objects.all().values()
#     # queryset = Sensor.objects.prefetch_related('measurements').all()
#     serializer_class = SensorSerializer
#
# class PersonalView(APIView):
#     def get(self, request):
#         lst = Sensor.objects.all().values()
#         snd =
#         return Response({'sensor': list(lst)})





