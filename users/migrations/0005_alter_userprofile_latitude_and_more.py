# Generated by Django 5.0.1 on 2024-02-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude'),
        ),
    ]
