# Generated by Django 2.2.6 on 2019-11-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='coordinate_left',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='design',
            name='coordinate_top',
            field=models.CharField(max_length=30),
        ),
    ]
