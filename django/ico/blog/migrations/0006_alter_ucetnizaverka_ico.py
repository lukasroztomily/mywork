# Generated by Django 3.2.5 on 2022-01-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_ucetnizaverka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucetnizaverka',
            name='ico',
            field=models.CharField(max_length=90),
        ),
    ]
