# Generated by Django 3.1 on 2019-10-23 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191023_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='artwork_id',
            new_name='artwork',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='artwork_id',
            new_name='artwork',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='user_id',
            new_name='user',
        ),
    ]
