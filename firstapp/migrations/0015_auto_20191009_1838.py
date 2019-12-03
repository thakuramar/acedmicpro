# Generated by Django 2.2.6 on 2019-10-09 23:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_auto_20191009_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, default='DEFAULT VALUE', unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
