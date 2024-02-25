from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cursos.models import Curso #Para que a API acesse os campos que temos na model dos cursos
from rest_api.serializers import CursoModelSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def api(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    else:
        return Response({'message': 'Hello, API!'})
    
class CursoModelViewSet(ModelViewSet): #Permitindo que outras plataformas acessem os dados
    queryset = Curso.objects.all() 
    serializer_class = CursoModelSerializer
    
    