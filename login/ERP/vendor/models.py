from django.db import models

# Create your models here.

class VendorRegistration(models.Model):
    v_service_type = models.CharField(max_length=15,null=True)
    v_company_name = models.EmailField(max_length=30,unique=True)
    v_name_of_authorized = models.CharField(max_length=30)
    v_email  = models.EmailField(max_length=30,unique=True)
    v_mobile= models.CharField(max_length=10,unique=True)
    v_fax_number = models.CharField(max_length=30)
    v_pan = models.CharField(max_length=10)
    v_company_reg_number = models.CharField(max_length=30)
    v_company_gst_number = models.CharField(max_length=30)
    v_company_reg_date = models.DateTimeField()
    v_company_validity_date = models.DateTimeField()
    v_company_reg_address_line1 = models.CharField(max_length=30)
    v_company_reg_address_line2 = models.CharField(max_length=30)
    v_company_reg_address_city = models.CharField(max_length=30)
    v_company_reg_address_state = models.CharField(max_length=30)
    v_company_reg_address_district = models.CharField(max_length=30)
    v_company_reg_address_pincode = models.CharField(max_length=6)
    v_company_cor_address_line1 = models.CharField(max_length=30)
    v_company_cor_address_line2 = models.CharField(max_length=30)
    v_company_cor_address_city = models.CharField(max_length=30)
    v_company_cor_address_state = models.CharField(max_length=30)
    v_company_cor_address_district = models.CharField(max_length=30)
    v_company_cor_address_pincode = models.CharField(max_length=6)
    v_name_of_authorized_aadhar = models.CharField(max_length=15)
    v_name_of_authorized_dob = models.CharField(max_length=15)
    v_company_auth_address_line1 = models.CharField(max_length=30)
    v_company_auth_address_line2 = models.CharField(max_length=30)
    v_company_auth_address_state = models.CharField(max_length=30)
    v_company_auth_address_district = models.CharField(max_length=30)
    v_company_auth_address_pincode = models.CharField(max_length=6)
 
    v_company_dir_cor_address_line1 = models.CharField(max_length=30)
    v_company_dir_cor_address_line2 = models.CharField(max_length=30)
    v_company_dir_cor_address_city = models.CharField(max_length=30)
    v_company_dir_cor_address_state = models.CharField(max_length=30)

    v_company_dir_cor_address_pincode = models.CharField(max_length=6)

    v_company_dir_name = models.CharField(max_length=30)
    v_company_dir_name_hindi = models.CharField(max_length=30)
    v_company_dir_email = models.CharField(max_length=30)
    v_company_dir_aadhar= models.CharField(max_length=30,null=True,blank=True)
    v_company_dir_dob = models.CharField(max_length=30)
    v_company_dir_mobile = models.CharField(max_length=30)
    v_bank_name = models.CharField(max_length=30)
    v_bank_ifsc = models.CharField(max_length=30)
    v_bank_ac_holder_name = models.CharField(max_length=30)
    v_bank_ac_number = models.CharField(max_length=30)
    v_bank_ac_number_re_enter = models.CharField(max_length=30)
    






# class Company_Details(models.Model):
#     V_id = models.ForeignKey(Vendor, default="", on_delete=models.CASCADE)
#     C_Name_E = models.CharField(max_length=50)
#     C_Name_H = models.CharField(max_length=50)
#     C_Contact_No = models.CharField(max_length=13)
#     C_Fax_No = models.CharField(max_length=13)
#     Created_by = models.CharField(max_length=50)
#     Created_date = models.DateTimeField(auto_now_add=True)
#     Disabled_date = models.DateField(default=timezone.now)
#     Enable_date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return self.C_Name_E

# class Vendor_Authorised_Person_Info(models.Model):
#     Gender = models.CharField(max_length=50)
#     E_Name = models.CharField(max_length=50)
#     H_Name = models.CharField(max_length=50)
#     DOB = models.DateField(default=timezone.now)
#     # Contact_no Used for identification purposes
#     Contact_no = models.CharField(max_length=13)
#     email = models.CharField(max_length=100)
#     aadhar = models.CharField(max_length=13)
#     Created_by = models.CharField(max_length=50)
#     Created_date = models.DateTimeField(auto_now_add=True)
#     Disabled_date = models.DateField(default=timezone.now)
#     Enable_date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return self.Contact_no

# class VendorLogin(models.Model):
#     Contact_no = models.CharField(max_length=13)
#     email = models.CharField(max_length=100)
#     Temporary_Password = models.CharField(10)
#     OTP = models.CharField(6)

#     def __str__(self):
#         return self.Contact_no
    

  

    
