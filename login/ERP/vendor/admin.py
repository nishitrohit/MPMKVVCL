from django.contrib import admin

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
        "v_existing_pan",
        "v_upload_file",
        "v_upload_file_father",
        "v_upload_file_mother",
        "v_upload_file_factory"


    )
    list_filter = (
        'v_company_name',
        'v_email',
   )

@admin.register(finance_officer)
class Finance_OfficerAdmin(admin.ModelAdmin):
    list_display = (
        "v_company_name",
        "verified"
       
    )
    list_filter= (
         "v_company_name",
         "verified"
    )

@admin.register(working_officer)
class Working_OfficerAdmin(admin.ModelAdmin):
    list_display = (
        "v_company_name",
        "verified"
       
    )
    list_filter= (
         "v_company_name",
         "verified"
    )



@admin.register(officer)
class officerAdmin(admin.ModelAdmin):

    list_display = (
        "v_company_name",
        "verified",
        "po_number"

    )
    list_filter = (
        
        'verified',
        'po_number'
   )


@admin.register(dispatch)
class DispatchAdmin(admin.ModelAdmin):

    list_display = (
        "material_name",
        "po_number"

    )
    list_filter = (
        'material_name',
        'po_number'
       
   )


@admin.register(my_order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "v_company_name",
        "po_number"

    )
    list_filter = (
        'v_company_name',
        'po_number'
       
   )

@admin.register(TkcLogin)
class TkcLoginAdmin(admin.ModelAdmin):
    list_display = (
        "v_service_type",
        "C_Name",
        "Contact_no"
       
    )
    list_filter= (
         "v_service_type",
         "C_Name",
         "Contact_no"
    )


# @admin.register(Company_Details)
# class Company_DetailsAdmin(admin.ModelAdmin):
#     list_display = (
#         "C_Contact_No",
#         "C_Fax_No",
#         "C_Pan_No"
       
#     )
#     list_filter= (
#         "C_Contact_No",
#         "C_Fax_No",
#         "C_Pan_No"
#     )



# @admin.register(Address)
# class Company_DetailsAdmin(admin.ModelAdmin):
#     list_display = (
#         "Line_1",
#         "Line_2",
#         "C_Contact_No"
       
#     )
#     list_filter= (
#         "Line_1",
#         "Line_2",
#         "C_Contact_No"
#     )
