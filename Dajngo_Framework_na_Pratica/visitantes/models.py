from django.db import models
from django.utils import timezone


class Visitantes(models.Model):
    nome = models.CharField(
        max_length=129,
        verbose_name="Nome completo",
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF do visitante",
    )

    data_nascimento_visitante = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
        default="1900-01-01"
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada",
        default=0,
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veículo do visitante",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=False,
        blank=True,
        null=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saida do visitante",
        auto_now=False,
        blank=True,
        null=True,
        default=None,
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now_add=False,
        blank=True,
        null=True,
    )

    morador_responsavel_do_visitante = models.CharField(
        verbose_name="Morador responsavel",
        max_length=198,
        blank=True,
    )

    autorizado = models.BooleanField(
        verbose_name="Visitante autorizado? ",
        default=False,
    )

    def save(self, *args, **kwargs):
        # Se o visitante for autorizado e ainda não tiver horário de autorização
        if self.autorizado and not self.horario_autorizacao:
            self.horario_autorizacao = timezone.now()

        if self.horario_autorizacao is not None and self.horario_saida is None:
            self.autorizado = True

        if self.horario_saida is not None:
            self.autorizado = False

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"

    def __str__(self):
        return f"ID: {self.pk} - {self.nome}"
