# Generated by Django 3.2.5 on 2022-01-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='headline_de',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='blog',
            name='headline_en',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='blog',
            name='headline_sk',
            field=models.CharField(max_length=150),
        ),
    ]
