# Generated by Django 5.0.1 on 2024-02-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0013_alter_built_furnished_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=50)),
            ],
        ),
    ]
