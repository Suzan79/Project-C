# Generated by Django 2.2.6 on 2019-12-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20191218_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderartwork',
            name='artwork_price',
            field=models.DecimalField(decimal_places=2, default=24.99, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='orderartwork',
            name='artwork_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product_name',
            field=models.CharField(default='', max_length=60),
        ),
    ]
