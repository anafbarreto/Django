from django.urls import path
from rest_api.views import api
from rest_framework.routers import SimpleRouter 
from rest_api.views import CursoModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False) # O simple router por padrão adiciona / no final das urls, e o trailing_slash vai permitir que as urls sejam escritas sem o /
router.register('cursos', CursoModelViewSet) # Definindo a rota



urlpatterns = [
    path('api/', api),
]

urlpatterns += router.urls 