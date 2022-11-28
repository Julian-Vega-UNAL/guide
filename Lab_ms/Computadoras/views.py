
from rest_framework.viewsets import ModelViewSet
from Computadoras.serializers import ProcesadorSerializer, EmpresaSerializer, ComputadorasSerializer
from Computadoras.models import Procesador, Empresa, Computadoras
# Create your views here.
class ProcesadorApiViewSet(ModelViewSet):
    serializer_class = ProcesadorSerializer
    queryset = Procesador.objects.all()
    
class EmpresaApiViewSet(ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    
class ComputadorasApiViewSet(ModelViewSet):
    serializer_class = ComputadorasSerializer
    queryset = Computadoras.objects.all()
    
    