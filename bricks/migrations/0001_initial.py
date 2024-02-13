# Generated by Django 5.0.1 on 2024-02-12 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('rent', 'Rent'), ('sale', 'Sale'), ('resale', 'Resale'), ('pg', 'PG'), ('on_lease', 'On Lease')], max_length=50)),
            ],
        ),
    ]
