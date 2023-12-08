# Generated by Django 5.0 on 2023-12-08 00:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitantes',
            options={'verbose_name': 'Visitante', 'verbose_name_plural': 'Visitantes'},
        ),
        migrations.RemoveField(
            model_name='visitantes',
            name='sobrenome',
        ),
        migrations.AddField(
            model_name='visitantes',
            name='data_nascimento_visitante',
            field=models.DateField(default='1900-01-01', verbose_name='Data de nascimento'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='horario_autorizacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário de autorização de entrada'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='horario_chegada',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Horário de chegada na portaria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitantes',
            name='horario_saida',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Horário de saida do visitante'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='morador_responsavel_do_visitante',
            field=models.CharField(blank=True, max_length=198, verbose_name='Morador responsavel pela autorização'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='numero_casa',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número da casa a ser visitada'),
        ),
        migrations.AddField(
            model_name='visitantes',
            name='placa_veiculo',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do veículo do visitante'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='autorizado',
            field=models.BooleanField(default=False, verbose_name='O visitante está autorizado? '),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='nome',
            field=models.CharField(max_length=129, verbose_name='Nome completo'),
        ),
    ]
