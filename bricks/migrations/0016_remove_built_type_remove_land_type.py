# Generated by Django 5.0.1 on 2024-02-14 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0015_built_cat_land_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='built',
            name='type',
        ),
        migrations.RemoveField(
            model_name='land',
            name='type',
        ),
    ]