from core.models.veiculo import Veiculo
from rest_framework.viewsets import ModelViewSet

from core.models import Modelo
from core.serializers import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer