from django.urls import path

from contatos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/<int:id>', views.show, name='contato/show'),
    path('contato/buscar/', views.search, name='contato/search'),
    path('contatos/list/', views.list_contatos, name='vue-list'),

]
