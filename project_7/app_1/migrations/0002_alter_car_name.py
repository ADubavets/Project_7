# Generated by Django 5.1 on 2024-08-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Наименование автомобиля'),
        ),
    ]
