# Generated by Django 5.0.1 on 2024-02-14 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0019_alter_built_image_alter_land_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='built',
            name='rent',
        ),
    ]
