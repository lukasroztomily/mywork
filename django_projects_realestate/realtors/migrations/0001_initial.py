# Generated by Django 3.1.2 on 2021-03-04 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phote', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(default=datetime.datetime(2021, 3, 4, 11, 59, 44, 803444))),
            ],
        ),
    ]
