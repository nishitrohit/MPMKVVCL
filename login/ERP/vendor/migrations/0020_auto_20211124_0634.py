# Generated by Django 3.2.9 on 2021-11-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0019_auto_20211123_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='finance_officer',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='working_officer',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]