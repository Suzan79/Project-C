# Generated by Django 2.2.6 on 2020-01-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_auto_20200101_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]