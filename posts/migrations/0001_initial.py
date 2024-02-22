# Generated by Django 4.0.5 on 2022-06-07 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 7, 22, 47, 28, 657817))),
            ],
        ),
        migrations.CreateModel(
            name='Put',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100000)),
                ('created_at',
                 models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 7, 22, 47, 28, 657817))),
            ],
        ),
    ]
