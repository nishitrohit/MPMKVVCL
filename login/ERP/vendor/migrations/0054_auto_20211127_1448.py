# Generated by Django 3.2.9 on 2021-11-27 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0053_auto_20211127_1252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tkc_Authorised_Person_Info',
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='aadhar',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='add1',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='add2',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='bank_ac_holder_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='bank_ac_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='bank_ac_number_re_enter',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='bank_ifsc',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='bank_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='company_dir_aadhar',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='company_dir_cor_address_line1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='company_dir_dob',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='company_dir_email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='company_dir_mobile',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='dob',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='existing_pan',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='experienc',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='pin',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='state_auth',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='three_years_income_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='three_years_income_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='three_years_income_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='three_years_tax_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='three_years_tax_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='three_years_tax_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='tkc_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='turnover',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='vcompany_dir_cor_address_city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='vcompany_dir_cor_address_line2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='vcompany_dir_cor_address_pincode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='vcompany_dir_cor_address_state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='vcompany_dir_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tkclogin',
            name='vcompany_dir_name_hindi',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 14, 48, 19, 617108), null=True),
        ),
        migrations.AlterField(
            model_name='dispatch',
            name='dispatch_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 14, 48, 19, 617124), null=True),
        ),
    ]
