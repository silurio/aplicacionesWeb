# Generated by Django 2.2.1 on 2019-05-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamflix', '0016_auto_20190524_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actores',
            field=models.ManyToManyField(to='streamflix.Actor'),
        ),
    ]