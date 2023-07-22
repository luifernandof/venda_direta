# venda_direta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # URL da página inicial
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('extrato/', views.extrato, name='extrato'),
    path('compras/', views.compras, name='compras'),
    path('rastreamento/', views.rastreamento, name='rastreamento'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('comissao/', views.comissao, name='comissao'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('marketing/', views.marketing, name='marketing'),
    path('suporte/', views.suporte, name='suporte'),
    path('atendimento/', views.atendimento, name='atendimento'),
    # Adicione outras URLs do aplicativo aqui, conforme necessário
]
