from apps.planos.models import Plano
from apps.planos.serializers import PlanoSerializer
from rest_framework import generics


class PlanoList(generics.ListCreateAPIView):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer


class PlanoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer