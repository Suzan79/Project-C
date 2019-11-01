# Generated by Django 3.1 on 2019-10-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting_name', models.CharField(max_length=60)),
                ('painter_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Testmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=60)),
            ],
        ),
    ]