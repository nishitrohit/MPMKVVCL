# Generated by Django 3.2.9 on 2021-11-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_auto_20211117_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='v_mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
