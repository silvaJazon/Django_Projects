from django.db import models


class Visitantes(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name="Nome"
    )

    sobrenome = models.CharField(
        max_length=50,
        verbose_name="Sobrenome",
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF do visitante",
    )

    autorizado = models.BooleanField(
        verbose_name="O visitante está autorizado? ",
        default=False,
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
