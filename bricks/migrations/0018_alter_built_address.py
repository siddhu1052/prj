# Generated by Django 5.0.1 on 2024-02-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0017_alter_built_image_alter_land_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='built',
            name='address',
            field=models.CharField(default=None, max_length=200, null=True, unique=True),
        ),
    ]
