# Generated by Django 2.2.6 on 2019-10-10 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_profile_rn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
