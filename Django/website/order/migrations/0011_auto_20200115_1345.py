# Generated by Django 2.2.6 on 2020-01-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200101_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistoryitem',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]