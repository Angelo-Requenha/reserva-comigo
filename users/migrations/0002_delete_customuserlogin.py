# Generated by Django 5.0.1 on 2024-01-29 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserLogin',
        ),
    ]
