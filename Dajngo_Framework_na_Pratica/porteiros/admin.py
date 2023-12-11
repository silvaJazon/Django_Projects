from porteiros.models import Porteiro
from django.contrib import admin


class PorteiroAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'telefone', 'data_nascimento', 'usuario_ativo', 'pk')
    list_filter = ('User__is_active',)
    ordering = ('-nome_completo',)

    def usuario_ativo(self, obj):
        return obj.User.is_active

    usuario_ativo.boolean = True
    usuario_ativo.short_description = 'Usuário Ativo'


admin.site.register(Porteiro, PorteiroAdmin)
