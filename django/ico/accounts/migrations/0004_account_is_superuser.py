# Generated by Django 3.2.5 on 2022-01-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_is_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
