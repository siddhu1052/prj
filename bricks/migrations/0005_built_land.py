# Generated by Django 5.0.1 on 2024-02-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0004_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='built',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default=None, max_length=200, unique=True)),
                ('area', models.IntegerField()),
                ('floors', models.IntegerField()),
                ('images', models.ImageField(unique=True, upload_to='media/')),
                ('status', models.CharField(choices=[('uc', 'Under Construction'), ('rtm', 'Reasy to move')], max_length=50)),
                ('faces', models.CharField(choices=[('E', 'east'), ('NE', 'North-East'), ('N', 'north'), ('NW', 'North-West'), ('W', 'west'), ('SW', 'South-West'), ('S', 'south'), ('SE', 'South-East')], max_length=50)),
                ('fs', models.CharField(choices=[('F', 'Furnished'), ('uf', 'Furnished')], max_length=50)),
                ('type_of_ownership', models.CharField(choices=[('ind', 'Independent'), ('wo', 'With Owner')], max_length=50)),
                ('Age', models.IntegerField()),
                ('rent', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default=None, max_length=200, unique=True)),
                ('images', models.ImageField(unique=True, upload_to='media/')),
                ('area', models.IntegerField()),
            ],
        ),
    ]
