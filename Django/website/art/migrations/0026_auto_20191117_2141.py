# Generated by Django 2.2.6 on 2019-11-17 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0025_auto_20191117_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='upload_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 17, 21, 41, 22, 223545), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='upload_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 17, 21, 41, 22, 224544), null=True),
        ),
    ]
