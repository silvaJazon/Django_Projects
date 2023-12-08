from django.contrib import admin
from .models import Visitantes


@admin.register(Visitantes)
class VisitantesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'cpf', 'autorizado', 'horario_chegada', 'morador_responsavel_do_visitante')
    search_fields = ('nome', 'cpf', 'pk')
    list_filter = ('nome', 'autorizado')
    ordering = ('-horario_chegada',)
    actions = ['limpar_datas_action']

    fieldsets = (
        ('Informaçoes do Visitante', {
            'fields': ('nome', 'cpf', 'data_nascimento_visitante', 'numero_casa', 'placa_veiculo',
                       'morador_responsavel_do_visitante', 'autorizado',)

        }),
        ('Informações de Tempo', {
            'fields': ('horario_chegada', 'horario_autorizacao', 'horario_saida'),
            'description': 'Limpar Datas dos Visitantes Selecionados',
        }),)

    def limpar_datas_action(self, request, queryset):
        for visitante in queryset:
            visitante.limpar_datas()

    limpar_datas_action.short_description = "Limpar Datas dos Visitantes Selecionados"


