# Converte os dados em instancias que da pra entender, como Json. E tambem faz o contrario.

from rest_framework.serializers import ModelSerializer
from cursos.models import Curso

class CursoModelSerializer(ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__' #Todos os campos