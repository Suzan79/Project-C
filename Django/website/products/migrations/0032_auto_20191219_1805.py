# Generated by Django 3.0 on 2019-12-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20191219_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designtextcoordinate',
            name='font',
            field=models.CharField(default='Roboto', max_length=300),
        ),
    ]
