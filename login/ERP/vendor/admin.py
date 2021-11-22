from django.contrib import admin
from .models import VendorRegistration
from .models import *


@admin.register(VendorRegistration)
class VendorRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "v_service_type",
        "v_company_name",
        "v_name_of_authorized",
        "v_email",
        "v_mobile",
        "v_fax_number",
        "v_pan",
        "v_company_reg_number",
        "v_company_gst_number", 
        "v_company_reg_date", 
        "v_company_validity_date",
        "v_company_reg_address_line1",
        "v_company_reg_address_line2", 
        "v_company_reg_address_city",
        "v_company_reg_address_state", 
        "v_company_reg_address_district",
        "v_company_reg_address_pincode",
        "v_company_cor_address_line1", 
        "v_company_cor_address_line2", 
        "v_company_cor_address_state", 
        "v_company_cor_address_district", 
        "v_company_cor_address_pincode", 
        "v_name_of_authorized_aadhar", 
        "v_name_of_authorized_dob", 
        "v_company_auth_address_line1", 
        "v_company_auth_address_line2", 
        "v_company_auth_address_state", 
        "v_company_auth_address_district", 
        "v_company_auth_address_pincode", 
    
        "v_company_dir_cor_address_line1", 
        "v_company_dir_cor_address_line2", 
        "v_company_dir_cor_address_city", 
        "v_company_dir_cor_address_state", 

        "v_company_dir_cor_address_pincode",

        "v_company_dir_name", 
        "v_company_dir_name_hindi", 
        "v_company_dir_email",
        "v_company_dir_aadhar",
        "v_company_dir_dob", 
        "v_company_dir_mobile",
        "v_bank_name", 
        "v_bank_ifsc", 
        "v_bank_ac_holder_name",
        "v_bank_ac_number", 
        "v_bank_ac_number_re_enter", 
        

        "v_experienc", 
        "v_turnover",
        "v_existing_pan"


    )
    list_filter = (
        'v_company_name',
        'v_email',
   )