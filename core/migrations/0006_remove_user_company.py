# Generated by Django 3.0.3 on 2020-03-01 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200301_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
    ]
