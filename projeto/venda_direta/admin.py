from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'genero', 'cidade', 'estado', 'tipo_cartao', 'aceitar_termos')
    list_filter = ('genero', 'estado', 'tipo_cartao', 'aceitar_termos')
    search_fields = ('nome', 'email', 'telefone')

admin.site.register(Usuario, UsuarioAdmin)
