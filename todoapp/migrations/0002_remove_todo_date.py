# Generated by Django 2.2.1 on 2019-05-18 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
    ]
