# Generated by Django 3.1.2 on 2020-10-27 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='owner',
        ),
    ]
