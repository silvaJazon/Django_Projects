from django.contrib import admin
from .models import Visitantes

@admin.register(Visitantes)
class VisitantesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'cpf', 'autorizado', 'morador_responsavel_do_visitante',
                    'registrado_por',)
    search_fields = ('nome', 'cpf', 'pk')
    list_filter = ('nome', 'autorizado')
    ordering = ('-horario_chegada',)
    actions = ['limpar_datas_action']

    fieldsets = (
        ('Informações do Visitante', {
            'fields': ('nome', 'cpf', 'data_nascimento_visitante', 'numero_casa', 'placa_veiculo',
                       'morador_responsavel_do_visitante', 'autorizado', 'registrado_por',)

        }),
        ('Informações de Tempo', {
            'fields': ('horario_chegada', 'horario_autorizacao', 'horario_saida'),
        }),)

    def limpar_datas_action(self, request, queryset):
        for visitante in queryset:
            visitante.limpar_datas()

    limpar_datas_action.short_description = "Limpar Datas dos Visitantes Selecionados"
