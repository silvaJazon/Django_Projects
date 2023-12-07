from django.contrib import admin
from visitantes.models import Visitantes


@admin.register(Visitantes)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'autorizado' )
    search_fields = ('nome', 'sobrenome', 'cpf')

