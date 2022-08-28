from unicodedata import name
from django.urls import path
from .views import lista_produtos, novo_produto, editar_produto, deletar_produto

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('novoproduto', novo_produto, name='novo_produto'),
    path('editarproduto/<int:id>/', editar_produto, name='editar_produto'),
    path('deletarproduto/<int:id>/', deletar_produto, name='deletar_produto'),
]