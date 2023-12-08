# Generated by Django 4.2.8 on 2023-12-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0003_alter_visitantes_horario_chegada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitantes',
            name='autorizado',
            field=models.BooleanField(default=False, verbose_name='Visitante autorizado? '),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='horario_chegada',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário de chegada na portaria'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='morador_responsavel_do_visitante',
            field=models.CharField(blank=True, max_length=120, verbose_name='Morador responsável'),
        ),
    ]