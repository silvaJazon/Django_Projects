from django.db import models


class Porteiro(models.Model):
    User = models.OneToOneField(
        "usuarios.User",
        verbose_name="Usuario",
        on_delete=models.PROTECT
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone de Contato",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self):
        return f"ID: {self.pk} - {self.nome_completo}"
