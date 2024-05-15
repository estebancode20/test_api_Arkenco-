from rest_framework import viewsets
from .models import Prospecto
from .serializer import ProspectoSerializer

# Create your views here.

class ProspectoViewSet(viewsets.ModelsViewset):
    queryset = Prospecto.objects.all()
    serializer_class = ProspectoSerializer

