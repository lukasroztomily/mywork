# Generated by Django 3.1.7 on 2021-05-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
