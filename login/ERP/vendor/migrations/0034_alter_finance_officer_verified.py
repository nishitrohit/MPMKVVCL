# Generated by Django 3.2.9 on 2021-11-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0033_auto_20211125_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_officer',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]