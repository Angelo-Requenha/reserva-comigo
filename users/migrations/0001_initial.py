# Generated by Django 5.0.1 on 2024-02-18 19:39

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tipo', models.CharField(choices=[('C', 'Cliente'), ('E', 'Estabelecimento')], default='C', max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='foto_perfil')),
                ('groups', models.ManyToManyField(related_name='customuser_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='customuser_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FotosEstab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('foto1', models.ImageField(blank=True, null=True, upload_to='foto_estab')),
                ('foto2', models.ImageField(blank=True, null=True, upload_to='foto_estab')),
                ('foto3', models.ImageField(blank=True, null=True, upload_to='foto_estab')),
                ('foto4', models.ImageField(blank=True, null=True, upload_to='foto_estab')),
                ('foto5', models.ImageField(blank=True, null=True, upload_to='foto_estab')),
                ('foto6', models.ImageField(blank=True, null=True, upload_to='foto_estab')),
                ('has_fotos', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
                ('pais', models.CharField(blank=True, max_length=255, null=True, verbose_name='País')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('valor_aluguel', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('capacidade_pessoas', models.PositiveIntegerField(default=0)),
                ('tipo_horario', models.CharField(choices=[('hora', 'Por Hora'), ('noite', 'Por Noite')], default='hora', max_length=5)),
                ('has_profile', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
