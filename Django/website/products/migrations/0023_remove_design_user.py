# Generated by Django 2.2.6 on 2019-12-03 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20191203_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='user',
        ),
    ]
