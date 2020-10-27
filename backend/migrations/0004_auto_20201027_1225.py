# Generated by Django 3.1.2 on 2020-10-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_farm_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='crop_type',
            field=models.CharField(blank=True, choices=[('FR', 'Fruit'), ('VG', 'Vegetable'), ('PL', 'Pulse'), ('SP', 'Spice')], max_length=2, null=True),
        ),
    ]
