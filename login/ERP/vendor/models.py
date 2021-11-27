from django.db import models

# Create your models here.

class VendorRegistration(models.Model):
    v_service_type = models.CharField(max_length=15,null=True)
    v_company_name = models.CharField(max_length=30,unique=True,primary_key=True)
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
    v_upload_file = models.ImageField(upload_to="images/",null=True)
    v_father_aadhar_name = models.CharField(max_length=15,null=True,blank=True)
    v_father_number = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file_father = models.ImageField(upload_to="images/",null=True)
    v_mother_aadhar_name = models.CharField(max_length=15,null=True,blank=True)
    v_mother_number = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file_mother = models.ImageField(upload_to="images/",null=True)
    v_area_occupied = models.CharField(max_length=15,null=True,blank=True)
    v_working_shift = models.CharField(max_length=15,null=True,blank=True)
    v_personal_work_factroyr = models.CharField(max_length=15,null=True,blank=True)
    v_buit_up = models.CharField(max_length=15,null=True,blank=True)
    v_product_capacity = models.CharField(max_length=15,null=True,blank=True)
    v_faculty_license_number = models.CharField(max_length=15,null=True,blank=True)
    v_upload_file_factory = models.ImageField(upload_to="images/",null=True)
    
    v_e_office_name= models.CharField(max_length=30,null=True,blank=True)
    v_test_type_report= models.CharField(max_length=30,null=True,blank=True)
    v_upload_file_media = models.ImageField(upload_to="images/",null=True)
    v_gtp_drawing= models.CharField(max_length=30,null=True,blank=True)
    v_upload_file_e = models.ImageField(upload_to="images/",null=True)
    v_office_name_supply= models.CharField(max_length=30,null=True,blank=True)
    v_supply_criteria= models.CharField(max_length=30,null=True,blank=True)
    v_upload_file_ele = models.ImageField(upload_to="images/",null=True)
    v_office_name_list= models.CharField(max_length=30,null=True,blank=True)
    v_list_plants= models.CharField(max_length=30,null=True,blank=True)
    v_file_upload_elev = models.ImageField(upload_to="images/",null=True)
    v_list_testing= models.CharField(max_length=30,null=True,blank=True)
    v_list_testing_eqi= models.CharField(max_length=30,null=True,blank=True)
    v_upload_file_eleve = models.ImageField(upload_to="images/",null=True)
    v_office_name_calib= models.CharField(max_length=30,null=True,blank=True)
    v_alibration= models.CharField(max_length=30,null=True,blank=True)
    v_file_upload_eleven = models.ImageField(upload_to="images/",null=True)
    v_office_name_bis= models.CharField(max_length=30,null=True,blank=True)
    v_bis_license_no= models.CharField(max_length=30,null=True,blank=True)
    v_upload_se = models.ImageField(upload_to="images/",null=True)
    v_office_eight= models.CharField(max_length=30,null=True,blank=True)
    v_isi_licence= models.CharField(max_length=30,null=True,blank=True)
    v_upload_eight = models.ImageField(upload_to="images/",null=True)
    v_office_name_nine= models.CharField(max_length=30,null=True,blank=True)
    v_product_nine= models.CharField(max_length=30,null=True,blank=True)
    v_upload_nine = models.ImageField(upload_to="images/",null=True)
    v_office_name_ten= models.CharField(max_length=30,null=True,blank=True)
    v_method_ten= models.CharField(max_length=30,null=True,blank=True)
    v_upload_ten = models.ImageField(upload_to="images/",null=True)
    v_office_name_one = models.CharField(max_length=30,null=True,blank=True)
    v_eleven_source= models.CharField(max_length=30,null=True,blank=True)
    v_eleven_upload_one = models.ImageField(upload_to="images/",null=True)
    v_office_name_two= models.CharField(max_length=30,null=True,blank=True)
    v_office_list_two= models.CharField(max_length=30,null=True,blank=True)
    v_upload_file_two = models.ImageField(upload_to="images/",null=True)

    v_three_years_income_1 = models.CharField(max_length=30,null=True,blank=True)
    v_three_years_income_2 = models.CharField(max_length=30,null=True,blank=True)
    v_three_years_income_3= models.CharField(max_length=30,null=True,blank=True)
    v_three_years_tax_1= models.CharField(max_length=30,null=True,blank=True)
    v_three_years_tax_2= models.CharField(max_length=30,null=True,blank=True)
    v_three_years_tax_3= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_1= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_2= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_1_upload= models.ImageField(upload_to="images/",null=True)
    v_balance_sheet_3= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_4= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_2_upload= models.ImageField(upload_to="images/",null=True)
    v_balance_sheet_5= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_6= models.CharField(max_length=30,null=True,blank=True)
    v_balance_sheet_3_upload= models.ImageField(upload_to="images/",null=True)
    v_profit_loss_sheet_1= models.CharField(max_length=30,null=True,blank=True)
    v_profit_loss_sheet_2= models.CharField(max_length=30,null=True,blank=True)
    v_profit_loss_sheet_1_upload= models.ImageField(upload_to="images/",null=True)
    v_profit_loss_sheet_3= models.CharField(max_length=30,null=True,blank=True)
    v_profit_loss_sheet_4= models.CharField(max_length=30,null=True,blank=True)
    v_profit_loss_sheet_2_upload= models.ImageField(upload_to="images/",null=True)
    v_profit_loss_sheet_5= models.CharField(max_length=30,null=True,blank=True)
    v_profit_loss_sheet_6= models.CharField(max_length=30,null=True,blank=True)
    v_profit_loss_sheet_3_upload= models.ImageField(upload_to="images/",null=True)
    v_pan_name_t= models.CharField(max_length=30,null=True,blank=True)
    v_pan_number_t= models.CharField(max_length=30,null=True,blank=True)
    v_pan_issue_t= models.CharField(max_length=30,null=True,blank=True)
    v_pan_issue_t_upload= models.ImageField(upload_to="images/",null=True)
    v_income_tax_return_name= models.CharField(max_length=30,null=True,blank=True)
    v_income_tax_return_number= models.CharField(max_length=30,null=True,blank=True)
    v_income_tax_return_name_doc_upload= models.ImageField(upload_to="images/",null=True)
    v_gst_number_state= models.CharField(max_length=30,null=True,blank=True)
    v_gst_serial_number= models.CharField(max_length=30,null=True,blank=True)
    v_gst_doc_upload = models.ImageField(upload_to="images/",null=True)
    v_verified_by_financne = models.BooleanField(default=False)
    v_verified_by_working = models.BooleanField(default=False)

    def __str__(self):
        return self.v_service_type


class finance_officer(models.Model):
    # v_company_name = models.ForeignKey(VendorRegistration,on_delete=models.CASCADE)
    v_company_name = models.CharField(max_length=30,null=True,blank=True)
    user_name = models.CharField(max_length=10,null=True,blank=True,default="finance")
    password = models.CharField(max_length=10,null=True,blank=True,default="12345")
    verified = models.BooleanField(default=False,null=True)

    v_file_upload_eleven = models.ImageField(upload_to="images/",null=True)
    v_file_upload = models.ImageField(upload_to="images/",null=True)

class working_officer(models.Model):
    v_company_name = models.CharField(max_length=30,null=True,blank=True)
    user_name = models.CharField(max_length=10,null=True,blank=True,default="working")
    password = models.CharField(max_length=10,null=True,blank=True,default="12345")
    verified = models.BooleanField(default=False,null=True)

    incode_first_year = models.CharField(max_length=30,null=True,blank=True)
    incode_secound_year = models.CharField(max_length=30,null=True,blank=True)


class officer(models.Model):
    v_company_name = models.CharField(max_length=30,null=True,blank=True)
    user_name = models.CharField(max_length=10,null=True,blank=True,default="working")
    password = models.CharField(max_length=10,null=True,blank=True,default="12345")
    verified = models.BooleanField(default=False)
    v_name_of_authorized = models.CharField(max_length=30,null=True,blank=True)
  
 














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

    def __str__(self):
        return self.Contact_no
    


# class Nabl_login(models.Model):
#     Nabl_id=models.AutoField(primary_key=True)
#     Nabl_login_id=models.CharField(max_length=10)
#     Nabl_password=models.CharField(max_length=15)
#     Nabl_otp=models.CharField(max_length=6)
#     Nabl_verify_status=models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.Nabl_login_id


# class Nabl_Registration(models.Model):
#     Nabl_id=models.ForeignKey(Nabl_login,on_delete=models.CASCADE)
#     Nabl_ownership_id=models.CharField(max_length=30)
#     Nabl_authorisedperson_id=models.ForeignKey(Nabl_Authorisedperson,on_delete=models.CASCADE)
#     Nabl_contact_no=models.IntegerField(max_length=13)
#     Nabl_emailid=models.EmailField(max_length=30,unique=True)
#     Nabl_experience=models.IntegerField(max_length=4)
#     Nabl_turnover=models.IntegerField(max_length=20)
#     Nabl_pancard=models.CharField(max_length=10)
#     Nabl_aadhar=models.IntegerField(max_length=12)
#
#     def __str__(self):
#         return self.Nabl_emailid


class NablRegistration(models.Model):
    n_service_type = models.CharField(max_length=15, null=True)
    n_company_name = models.CharField(max_length=30, unique=True, primary_key=True)
    n_name_of_authorized = models.CharField(max_length=30)
    n_email = models.EmailField(max_length=30, unique=True)
    n_mobile = models.CharField(max_length=10, unique=True)
    n_company_reg_date = models.DateTimeField()
    n_company_validity_date = models.DateTimeField()

    n_fax_number = models.CharField(max_length=30, default="")
    n_pan = models.CharField(max_length=10, default="")
    n_company_reg_number = models.CharField(max_length=30, default="")
    n_company_gst_number = models.CharField(max_length=30, default="")
    n_company_reg_address_line1 = models.CharField(max_length=30, default="")
    n_company_reg_address_line2 = models.CharField(max_length=30, default="")
    n_company_reg_address_city = models.CharField(max_length=30, default="")
    n_company_reg_address_state = models.CharField(max_length=30, default="")
    n_company_reg_address_district = models.CharField(max_length=30, default="")
    n_company_reg_address_pincode = models.CharField(max_length=6, default="")
    n_company_cor_address_line1 = models.CharField(max_length=30, default="")
    n_company_cor_address_line2 = models.CharField(max_length=30, default="")
    n_company_cor_address_city = models.CharField(max_length=30, default="")
    n_company_cor_address_state = models.CharField(max_length=30, default="")
    n_company_cor_address_district = models.CharField(max_length=30, default="")
    n_company_cor_address_pincode = models.CharField(max_length=6, default="")
    n_name_of_authorized_aadhar = models.CharField(max_length=15, default="")
    n_name_of_authorized_dob = models.CharField(max_length=15, default="")
    n_company_auth_address_line1 = models.CharField(max_length=30, default="")
    n_company_auth_address_line2 = models.CharField(max_length=30, default="")
    n_company_auth_address_state = models.CharField(max_length=30, default="")
    n_company_auth_address_district = models.CharField(max_length=30, default="")
    n_company_auth_address_pincode = models.CharField(max_length=6, default="")

    n_company_dir_cor_address_line1 = models.CharField(max_length=30,default="" )
    n_company_dir_cor_address_line2 = models.CharField(max_length=30,default="" )
    n_company_dir_cor_address_city = models.CharField(max_length=30,default="" )
    n_company_dir_cor_address_state = models.CharField(max_length=30,default="" )

    n_company_dir_cor_address_pincode = models.CharField(max_length=6,default="" )

    n_company_dir_name = models.CharField(max_length=30,default="")
    n_company_dir_name_hindi = models.CharField(max_length=30,default="")
    n_company_dir_email = models.CharField(max_length=30,default="")
    n_company_dir_aadhar= models.CharField(max_length=30,null=True,blank=True,default="")
    n_company_dir_dob = models.CharField(max_length=30,default="")
    n_company_dir_mobile = models.CharField(max_length=30,default="")
    n_bank_name = models.CharField(max_length=30,default="")
    n_bank_ifsc = models.CharField(max_length=30,default="")
    n_bank_ac_holder_name = models.CharField(max_length=30,default="")
    n_bank_ac_number = models.CharField(max_length=30,default="")
    n_bank_ac_number_re_enter = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.n_service_type
