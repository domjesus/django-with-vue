from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_categoria


class Contato(models.Model):

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    show_on_list = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')


