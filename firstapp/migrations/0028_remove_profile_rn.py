# Generated by Django 2.2.6 on 2019-10-10 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0027_auto_20191009_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rn',
        ),
    ]
