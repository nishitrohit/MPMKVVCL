from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display=('v_service_type','v_company_name','v_name_of_authorized','v_email','v_mobile')

admin.site.register(VendorRegistration,UserRegistrationAdmin)