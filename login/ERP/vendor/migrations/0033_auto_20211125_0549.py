# Generated by Django 3.2.9 on 2021-11-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0032_auto_20211125_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finance_officer',
            name='v_name_of_authorized',
        ),
        migrations.AlterField(
            model_name='finance_officer',
            name='password',
            field=models.CharField(blank=True, default='12345', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='finance_officer',
            name='user_name',
            field=models.CharField(blank=True, default='finance', max_length=10, null=True),
        ),
    ]
