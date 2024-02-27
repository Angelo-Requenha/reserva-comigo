# Generated by Django 5.0 on 2024-02-27 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do grupo')),
                ('ano', models.IntegerField(default=2024)),
                ('mes', models.IntegerField(default=2)),
                ('dia', models.IntegerField(default=29)),
                ('duracao', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('confirmado', 'Confirmado'), ('recusado', 'Recusado')], default='pendente', max_length=20)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('confirmado', 'Confirmado'), ('recusado', 'Recusado')], default='pendente', max_length=20)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente_app.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='StatusPagamentoMembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_pagamento', models.CharField(choices=[('pendente', 'Pendente'), ('Pago', 'Pago')], default='pendente', max_length=20)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente_app.grupo')),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='membros',
            field=models.ManyToManyField(through='cliente_app.StatusPagamentoMembro', to=settings.AUTH_USER_MODEL),
        ),
    ]
