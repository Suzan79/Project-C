# Generated by Django 3.1 on 2019-10-23 13:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20191023_1552'),
        ('art', '0008_auto_20191023_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('stock', models.IntegerField()),
                ('description', models.CharField(max_length=600)),
                ('price', models.IntegerField()),
                ('product_photo', models.ImageField(upload_to='')),
                ('upload_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('artwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.Artwork')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('artwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.Artwork')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
