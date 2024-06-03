from apps.planos.models import Plano, Aporte, Resgate
from apps.planos.serializers import PlanoSerializer, AporteSerializer, ResgateSerializer
from rest_framework import generics


class PlanoList(generics.ListCreateAPIView):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer


class PlanoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer


class AporteList(generics.ListCreateAPIView):
    queryset = Plano.objects.all()
    serializer_class = AporteSerializer


class AporteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aporte.objects.all()
    serializer_class = AporteSerializer


class ResgateList(generics.ListCreateAPIView):
    queryset = Plano.objects.all()
    serializer_class = ResgateSerializer


class ResgateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aporte.objects.all()
    serializer_class = ResgateSerializer