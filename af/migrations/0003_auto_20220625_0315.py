# Generated by Django 3.2 on 2022-06-25 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('af', '0002_auto_20220625_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jumiaproduct',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='jumiaproduct',
            name='price',
        ),
    ]
