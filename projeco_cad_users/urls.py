from django.urls import path
from app_cad_users import views

urlpatterns = [
    #rota, view resposável e nome de referência
    path("", views.home, name="home"),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
