# Generated by Django 3.2.9 on 2021-11-26 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0050_auto_20211126_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatch',
            name='disabled_date',
        ),
        migrations.AddField(
            model_name='dispatch',
            name='dispatch_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 13, 43, 27, 60627), null=True),
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 13, 43, 27, 60612), null=True),
        ),
    ]