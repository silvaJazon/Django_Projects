from django import forms
from visitantes.models import Visitantes


class visitanteForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = "__all__"
