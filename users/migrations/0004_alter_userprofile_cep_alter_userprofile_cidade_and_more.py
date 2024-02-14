# Generated by Django 4.2.6 on 2024-02-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cep',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cidade',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='estado',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pais',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='País'),
        ),
    ]
