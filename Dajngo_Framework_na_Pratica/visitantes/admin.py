from django.contrib import admin
from .models import Visitantes

@admin.register(Visitantes)
class VisitantesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'cpf', 'autorizado', 'horario_chegada','morador_responsavel_do_visitante')
    search_fields = ('nome', 'cpf', 'pk')
    list_filter = ('autorizado',)
    ordering = ('-horario_chegada',)

    fieldsets = (
        ('Informaçoes do Visitante',{
            'fields': ('nome', 'cpf', 'data_nascimento_visitante', 'numero_casa', 'placa_veiculo', 'autorizado')
        }),
        ('Informações de Tempo', {
            'fields': ('horario_chegada','horario_autorizacao', 'horario_saida'),
        }),
        ('Detalhes Adicionais', {
            'fields': ('morador_responsavel_do_visitante',),
        }),
    )

    readonly_fields = ('horario_chegada',)
