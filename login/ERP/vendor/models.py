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
    

    v_experienc = models.CharField(max_length=3,null=True,blank=True)
    v_turnover = models.CharField(max_length=15,null=True,blank=True)

    v_existing_pan = models.CharField(max_length=10,null=True,blank=True)

    v_office_name  = models.CharField(max_length=15,null=True,blank=True)
    v_dic_reg_num = models.CharField(max_length=15,null=True,blank=True)
    v_issue_date = models.CharField(max_length=15,null=True,blank=True)
    v_end_date = models.CharField(max_length=15,null=True,blank=True)
    v_p_aadhar_hoder_name = models.CharField(max_length=15,null=True,blank=True)
    v_p_aadhar_reg_number = models.CharField(max_length=15,null=True,blank=True)
    v_p_issue_date = models.CharField(max_length=15,null=True,blank=True)
    v_p_a_end_date = models.CharField(max_length=15,null=True,blank=True)
    v_p_office_name = models.CharField(max_length=15,null=True,blank=True)
    v_p_reg_number = models.CharField(max_length=15,null=True,blank=True)
    v_p_end_date = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file = models.ImageField(upload_to="img",null=True)
    v_father_aadhar_name = models.CharField(max_length=15,null=True,blank=True)
    v_father_number = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file_father = models.ImageField(upload_to="img",null=True)
    v_mother_aadhar_name = models.CharField(max_length=15,null=True,blank=True)
    v_mother_number = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file_mother = models.ImageField(upload_to="img",null=True)
    v_area_occupied = models.CharField(max_length=15,null=True,blank=True)
    v_working_shift = models.CharField(max_length=15,null=True,blank=True)
    v_personal_work_factroyr = models.CharField(max_length=15,null=True,blank=True)
    v_buit_up = models.CharField(max_length=15,null=True,blank=True)
    v_product_capacity = models.CharField(max_length=15,null=True,blank=True)
    v_faculty_license_number = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file_factory = models.ImageField(upload_to="img",null=True)
    def __str__(self):
        return self.v_service_type

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
    

  

    
