# Generated by Django 3.2.9 on 2021-11-26 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0049_auto_20211126_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='officer',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='officer',
            name='v_name_of_authorized',
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 13, 4, 46, 178209), null=True),
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='disabled_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 26, 13, 4, 46, 178224), null=True),
        ),
    ]