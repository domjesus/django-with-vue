from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email','show_on_list')
    list_editable = ('telefone', 'show_on_list')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
