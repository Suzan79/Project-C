# Generated by Django 3.1 on 2019-10-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20191011_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='no email', max_length=60),
            preserve_default=False,
        ),
    ]