# Generated by Django 3.1.2 on 2020-11-03 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destino', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ciudad',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='destino',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='destino',
            name='url',
        ),
    ]
