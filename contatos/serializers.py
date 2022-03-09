from rest_framework import routers,serializers,viewsets
from .models import Contato
class ContatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'sobrenome', 'telefone', 'email', 'descricao', 'data_criacao','categoria_id']