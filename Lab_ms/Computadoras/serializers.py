
from rest_framework.serializers import ModelSerializer
from Computadoras.models import Procesador, Empresa, Computadoras

class ProcesadorSerializer(ModelSerializer):
    class Meta:
        model = Procesador
        fields = ['Id_procesador', 'Nombre_procesador']

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['Id_empresa', 'Nombre_empresa', 'Sede_central', 'Tipo', 'Sitio_web']
            
class ComputadorasSerializer(ModelSerializer):
    class Meta:
        model = Computadoras
        fields = ['Id_computadora', 'Nombre_computadora', 'Medidas', 'RAM', 'Disco_solido', 'Color', 'Unidades_disponibles', 'Procesador', 'Empresa']
        
