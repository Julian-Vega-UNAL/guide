from rest_framework.routers import DefaultRouter
from Computadoras.views import ProcesadorApiViewSet, EmpresaApiViewSet, ComputadorasApiViewSet

router_Api = DefaultRouter()


router_Api.register(prefix='Computadoras', basename='Computadoras', viewset=ComputadorasApiViewSet)
router_Api.register(prefix='Empresa', basename='Empresa', viewset=EmpresaApiViewSet)
router_Api.register(prefix='Procesador', basename='Procesador', viewset=ProcesadorApiViewSet)

