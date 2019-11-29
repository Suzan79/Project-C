# Generated by Django 2.2.6 on 2019-11-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20191123_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='rotation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='design',
            name='coordinate_left',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='design',
            name='coordinate_top',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='design',
            name='height',
            field=models.IntegerField(default=300),
        ),
    ]