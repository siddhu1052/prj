# Generated by Django 5.0.2 on 2024-02-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0026_built_owner_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='owner_name',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='land',
            name='owner_phone',
            field=models.IntegerField(null=True),
        ),
    ]
