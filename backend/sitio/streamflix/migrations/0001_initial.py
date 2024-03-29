# Generated by Django 2.2.1 on 2019-05-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('A', 'Administrador'), ('U', 'Usuario')], default='U', max_length=2)),
            ],
        ),
    ]
