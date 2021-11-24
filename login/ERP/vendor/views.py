from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import *
from .serializer import  *
from django.views.generic import FormView
import json
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import datetime
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import random,math
from copy import deepcopy

def Login(request):
    # if request.method == 'POST':
    #     return HttpResponse("We are working on Dashboard")
        # if VendorRegistration.objects.filter(type=request.POST['type']):
        #     if VendorRegistration.objects.filter(username=request.POST['username']):
        #         if VendorRegistration.objects.filter(password1=request.POST['password']):
        #             res = VendorRegistration.objects.filter(type=request.POST['type'],username=request.POST['username'],
        #                                                     password1=request.POST['password'])
        #             if res:
        #                 request.session['uid'] = request.POST['username']
        #                 a= request.session['uid']
        #                 aa = VendorRegistration.objects.filter(username=request.session["uid"])   
        #                 cc = VendorRegistration_Serializer(aa,many=True)
        #                 dd = cc.data
        #                 ee = json.loads(json.dumps(dd))
        #                 tem = ee[-1]['temp']
        #                 print("helooool",tem)
        #                 if tem==True:
        #                     return redirect('dashboard')
        #                 else:
        #                     return HttpResponse("Admin not verifly your information please login after some time")
                        
        #         else:
        #             return render(request, 'vendor/login.html', {"msg": "invalid password"})
        #     else:
        #         return render(request, 'vendor/login.html', {"msg": "invalid username"})
    # else:
    #     return HttpResponse("We are working on Dashboard")
    return render(request, 'vendor/login.html')

  


def Registration(request):
  
    if request.method == "POST":   
        service_type = request.POST.get('service_type')     
        company_name = request.POST.get('company_name')
        name_of_authorized = request.POST.get('name_of_authorized')                        
        email = request.POST.get('email') 
        mobile = request.POST.get('mobile')  
        current_time = datetime.now()
        date_time = current_time.strftime("%d/%m/%Y %H:%M:%S")                      
  
        if VendorRegistration.objects.filter(v_email=email).exists():
            messages.warning(request,"email already register")
            return redirect('register')
   
        elif VendorRegistration.objects.filter(v_mobile=mobile).exists():
            return redirect('register')
     
        
        else:
            user_data = VendorRegistration(v_service_type=service_type,v_company_name=company_name,v_name_of_authorized=name_of_authorized,v_email=email,v_mobile=mobile,v_company_reg_date=current_time,v_company_validity_date=current_time)
            
            user_data.save()
            request.session['uid'] = request.POST['email']
            aaaaa= request.session['uid']
         
            # url = "https://www.fast2sms.com/dev/bulkV2"

            # payload = "message=This%20is%20a%20test%20message&language=english&route=q&numbers=9407820866"
            # headers = {
            #     'authorization': "FxOXbDJ3kKZRYH2pInuv5cigmLUWw9toEdq1zfTNSPy87heQ4AXHwf94UNnvzpjdcGmTeMZEQ0LJqYBD",
            #     'Content-Type': "application/x-www-form-urlencoded",
            #     'Cache-Control': "no-cache",
            #     }

            # response = requests.request("POST", url, data=payload, headers=headers)

            # print(response.text)
            return redirect('dashboard')
    return render(request,'vendor/vendor_reg1.html')



def Vendor_Registration_Two(request):
    if request.session.has_key('uid'):
        vendor_db = VendorRegistration.objects.filter(v_email=request.session['uid'])
        vendor_serializer =VendorRegistration_Serializer(vendor_db,many=True)
        data = vendor_serializer.data
        jsondata = json.loads(json.dumps(data))
        contact=jsondata[-1]['v_mobile']
        company_name =jsondata[-1]['v_company_name']
        business_type =jsondata[-1]['v_service_type']
        
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_fax_number= request.POST.get('fax')
            get_data.v_pan=request.POST.get('pan')
            get_data.v_company_reg_number=request.POST.get('reg_no')
            get_data.v_company_gst_number=request.POST.get('gst')
            get_data.v_company_reg_address_line1=request.POST.get('add1')
            get_data.v_company_reg_address_line2=request.POST.get('add2')
            get_data.v_company_reg_address_city=request.POST.get('city')
            get_data.v_company_reg_address_state=request.POST.get('state')
            get_data.v_company_reg_address_district=request.POST.get('district')
            get_data.v_company_reg_address_pincode=request.POST.get('zip')
            get_data.v_company_cor_address_line1=request.POST.get('add3')
            get_data.v_company_cor_address_line2=request.POST.get('add4')
            get_data.v_company_cor_address_city=request.POST.get('city2')
            get_data.v_company_cor_address_state=request.POST.get('state2')
            get_data.v_company_cor_address_district=request.POST.get('district2')
            get_data.v_company_cor_address_pincode=request.POST.get('zip2')
           
            get_data.save()
            return redirect("dashboard2")
    return render(request,'vendor/vendor_reg2.html',{"type":business_type,"cname":company_name,"mobile":contact})

def Vendor_Registration_Three(request):
    if request.session.has_key('uid'):
        vendor_db = VendorRegistration.objects.filter(v_email=request.session['uid'])
        vendor_serializer =VendorRegistration_Serializer(vendor_db,many=True)
        data = vendor_serializer.data
        jsondata = json.loads(json.dumps(data))
        contact=jsondata[-1]['v_mobile']
        auth_name =jsondata[-1]['v_name_of_authorized']
        email =jsondata[-1]['v_email']
        
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_name_of_authorized_dob= request.POST.get('dob')
            get_data.v_name_of_authorized_aadhar=request.POST.get('aadhar')
            get_data.v_company_auth_address_line1=request.POST.get('add5')
            get_data.v_company_auth_address_line2=request.POST.get('add6')
            get_data.v_company_auth_address_state=request.POST.get('state')

            get_data.v_company_auth_address_district= request.POST.get('district')
            get_data.v_company_auth_address_pincode=request.POST.get('zip')
            get_data.v_company_dir_name=request.POST.get('dir_name')
            get_data.v_company_dir_name_hindi=request.POST.get('dir_name_hindi')
            get_data.v_company_dir_dob=request.POST.get('dir_dob')

            get_data.v_company_dir_mobile= request.POST.get('dir_mobile')
            get_data.v_company_dir_email=request.POST.get('dir_email')
            get_data.v_company_dir_aadhar=request.POST.get('dir_aadhar')
            get_data.v_company_dir_cor_address_line1=request.POST.get('dir_add1')
            get_data.v_company_dir_cor_address_line2=request.POST.get('dir_add2')

            get_data.v_company_dir_cor_address_state= request.POST.get('dir_state')
            get_data.v_company_dir_cor_address_city=request.POST.get('dir_city')
            get_data.v_company_dir_cor_address_pincode=request.POST.get('dir_zip')
            
            get_data.save()
            return redirect("dashboard3")
    return render(request,'vendor/vendor_reg3.html',{"auth_name":auth_name,"mobile":contact,"email":email})

def Vendor_Registration_Four(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_bank_name= request.POST.get('bank_name')
            get_data.v_bank_ifsc=request.POST.get('ifsc')
            get_data.v_bank_ac_holder_name=request.POST.get('ac_holder_name')
            get_data.v_bank_ac_number=request.POST.get('ac_number')
            get_data.v_bank_ac_number_re_enter=request.POST.get('re_ac_number')
            get_data.save()
            return redirect("dashboard4")
    return render(request,'vendor/vendor_reg4.html')

def Vendor_Registration_Five(request):
    return render(request,'vendor/vendor_reg5.html')





def Vendor_Registration_Six(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 20000

        client = razorpay.Client(
            auth=("rzp_live_b8kvPyTH49V69F", "pl7ndE0ndRRyiYgbmH0cMyQ4"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def payment_success(request):
    return render(request, "success.html")


def Vendor_Registration_Seven(request):
    return render(request,'vendor/vendor_reg7.html')



def Vendor_Registration_Eight(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_experienc= request.POST.get('work_experience')
            get_data.v_turnover=request.POST.get('turn_over')
            get_data.save()
            return redirect("dashboard7")
    return render(request,'vendor/vendor_reg8.html')



def Vendor_Registration_Nine(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_existing_pan= request.POST.get('ac_number')
            get_data.save()
            return redirect("dashboard8")
    return render(request,'vendor/vendor_reg9.html')


def Vendor_Registration_Ten(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_office_name= request.POST.get('v_office_name')
            get_data.v_dic_reg_num=request.POST.get('v_dic_reg_num')
            get_data.v_issue_date=request.POST.get('v_issue_date')
            get_data.v_end_date=request.POST.get('v_end_date')
            get_data.v_p_aadhar_hoder_name=request.POST.get('v_p_aadhar_hoder_name')

            get_data.v_p_aadhar_reg_number= request.POST.get('v_p_aadhar_reg_number')
            get_data.v_p_issue_date=request.POST.get('v_p_issue_date')
            get_data.v_p_a_end_date=request.POST.get('v_p_a_end_date')
            get_data.v_p_office_name=request.POST.get('v_p_office_name')
            get_data.v_p_reg_number=request.POST.get('v_p_reg_number')

            get_data.v_p_end_date= request.POST.get('v_p_end_date')
            get_data.v_upload_file=request.FILES['v_upload_file']
            get_data.v_father_aadhar_name=request.POST.get('v_father_aadhar_name')
            get_data.v_father_number=request.POST.get('v_father_number')
            get_data.v_upload_file_father=request.FILES['v_upload_file_father']

            get_data.v_mother_aadhar_name= request.POST.get('v_mother_aadhar_name')
            get_data.v_mother_number=request.POST.get('v_mother_number')
            get_data.v_upload_file_mother=request.FILES['v_upload_file_mother']
            get_data.v_area_occupied=request.POST.get('v_area_occupied')
            get_data.v_working_shift=request.POST.get('v_working_shift')

            get_data.v_personal_work_factroyr= request.POST.get('v_personal_work_factroyr')
            get_data.v_buit_up=request.POST.get('v_buit_up')
            get_data.v_product_capacity=request.POST.get('v_product_capacity')
            get_data.v_faculty_license_number=request.POST.get('v_faculty_license_number')
            get_data.v_upload_file_factory=request.FILES['v_upload_file_factory']
            get_data.save()
            return redirect("dashboard9")
    return render(request,'vendor/vendor_reg10.html')



def Vendor_Registration_Eleven(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            
            get_data.v_e_office_name= request.POST.get('v_e_office_name')
            get_data.v_test_type_report=request.POST.get('v_test_type_report')
            get_data.v_upload_file_media=request.POST.get('v_upload_file_media')
            get_data.v_gtp_drawing=request.POST.get('v_gtp_drawing')
            get_data.v_upload_file_e=request.FILES['v_upload_file_e']
            
            get_data.v_office_name_supply= request.POST.get('v_office_name_supply')
            get_data.v_supply_criteria=request.POST.get('v_supply_criteria')
            get_data.v_upload_file_ele=request.FILES['v_upload_file_ele']
            get_data.v_office_name_list=request.POST.get('v_office_name_list')
            get_data.v_list_plants=request.POST.get('v_list_plants')
            
            get_data.v_file_upload_elev= request.FILES['v_file_upload_elev']
            get_data.v_list_testing=request.POST.get('v_list_testing')
            get_data.v_list_testing_eqi=request.POST.get('v_list_testing_eqi')
            get_data.v_upload_file_eleve=request.FILES['v_upload_file_eleve']
            get_data.v_office_name_calib=request.POST.get('v_office_name_calib')
            
            get_data.v_alibration= request.POST.get('v_alibration')
            get_data.v_file_upload_eleven=request.FILES['v_file_upload_eleven']
            get_data.v_office_name_bis=request.POST.get('v_office_name_bis')
            get_data.v_bis_license_no=request.POST.get('v_bis_license_no')
            get_data.v_upload_se=request.FILES['v_upload_se']
            
            get_data.v_office_eight= request.POST.get('v_office_eight')
            get_data.v_isi_licence=request.POST.get('v_isi_licence')
            get_data.v_upload_eight=request.FILES['v_upload_eight']
            get_data.v_office_name_nine=request.POST.get('v_office_name_nine')
            get_data.v_product_nine=request.POST.get('v_product_nine')
            
            get_data.v_upload_nine= request.FILES['v_upload_nine']
            get_data.v_office_name_ten=request.POST.get('v_office_name_ten')
            get_data.v_method_ten=request.POST.get('v_method_ten')
            get_data.v_upload_ten=request.FILES['v_upload_ten']
            get_data.v_office_name_one=request.POST.get('v_office_name_one')
            
            get_data.v_eleven_source= request.POST.get('v_eleven_source')
            get_data.v_eleven_upload_one=request.FILES['v_eleven_upload_one']
            get_data.v_office_name_two=request.POST.get('v_office_name_two')
            get_data.v_office_list_two=request.POST.get('v_office_list_two')
            get_data.v_upload_file_two=request.FILES['v_upload_file_two']
          
            get_data.save()
           
            return redirect("dashboard10")

    return render(request,'vendor/vendor_reg11.html')


def Vendor_Registration_Twelve(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            vendor_data=request.session['uid']
            get_data =VendorRegistration.objects.get(v_email=vendor_data)
            get_data.v_three_years_income_1= request.POST.get('v_three_years_income_1')
            get_data.v_three_years_income_2=request.POST.get('v_three_years_income_2')
            get_data.v_three_years_income_3=request.POST.get('v_three_years_income_3')
            get_data.v_three_years_tax_1=request.POST.get('v_three_years_tax_1')
            get_data.v_three_years_tax_2=request.POST.get('v_three_years_tax_2')

            get_data.v_three_years_tax_3= request.POST.get('v_three_years_tax_3')
            get_data.v_balance_sheet_1=request.POST.get('v_balance_sheet_1')
            get_data.v_balance_sheet_2=request.POST.get('v_balance_sheet_2')
            get_data.v_balance_sheet_1_upload=request.POST.get('v_balance_sheet_1_upload')
            get_data.v_balance_sheet_3=request.POST.get('v_balance_sheet_3')

            get_data.v_balance_sheet_4= request.POST.get('v_balance_sheet_4')
            get_data.v_balance_sheet_2_upload=request.POST.get('v_balance_sheet_2_upload')
            get_data.v_balance_sheet_5=request.POST.get('v_balance_sheet_5')
            get_data.v_balance_sheet_6=request.POST.get('v_balance_sheet_6')
            get_data.v_balance_sheet_3_upload=request.POST.get('v_balance_sheet_3_upload')

            get_data.v_profit_loss_sheet_1= request.POST.get('v_profit_loss_sheet_1')
            get_data.v_profit_loss_sheet_2=request.POST.get('v_profit_loss_sheet_2')
            get_data.v_profit_loss_sheet_1_upload=request.POST.get('v_profit_loss_sheet_1_upload')
            get_data.v_profit_loss_sheet_3=request.POST.get('v_profit_loss_sheet_3')
            get_data.v_profit_loss_sheet_4=request.POST.get('v_profit_loss_sheet_4')

            get_data.v_profit_loss_sheet_2_upload= request.POST.get('v_profit_loss_sheet_2_upload')
            get_data.v_profit_loss_sheet_5=request.POST.get('v_profit_loss_sheet_5')
            get_data.v_profit_loss_sheet_6=request.POST.get('v_profit_loss_sheet_6')
            get_data.v_profit_loss_sheet_3_upload=request.POST.get('v_profit_loss_sheet_3_upload')
           
            get_data.v_pan_name_t=request.POST.get('v_pan_name_t')

            get_data.v_pan_number_t= request.POST.get('v_pan_number_t')
            get_data.v_pan_issue_t=request.POST.get('v_pan_issue_t')
            get_data.v_pan_issue_t_upload=request.POST.get('v_pan_issue_t_upload')
            get_data.v_income_tax_return_name=request.POST.get('v_income_tax_return_name')
            get_data.v_income_tax_return_number=request.POST.get('v_income_tax_return_number')

            get_data.v_income_tax_return_name_doc_upload= request.POST.get('v_income_tax_return_name_doc_upload')
            get_data.v_gst_number_state=request.POST.get('v_gst_number_state')
            get_data.v_gst_serial_number=request.POST.get('v_gst_serial_number')
            get_data.v_gst_doc=request.POST.get('v_gst_doc')

            get_data.save()
            return redirect("dashboard11")

    return render(request,'vendor/vendor_reg12.html')


def Vendor_Registration_Thirteen(request):
    return render(request,'vendor/vendor_reg13.html')


def Vendor_Registration_Fourteen(request):
    if request.session.has_key('uid'):
        get_data=request.session['uid']
        
        vendor_table = VendorRegistration.objects.filter(v_email=get_data)
        
        vendor_serializer = VendorRegistration_Serializer(vendor_table,many=True)
        vendor_data = vendor_serializer.data
       
        aadhar_reg_no = vendor_data[0]['v_p_aadhar_reg_number']
        aadhar_father = vendor_data[0]['v_father_number']
        aadhar_mother = vendor_data[0]['v_mother_number']
        gst_state = vendor_data[0]['v_gst_number_state']
        gst_number = vendor_data[0]['v_gst_serial_number']
        
        sheet_o = vendor_data[0]['v_balance_sheet_1']
        sheet_t= vendor_data[0]['v_balance_sheet_2']
        sheet_th = vendor_data[0]['v_balance_sheet_3']
        sheet_f = vendor_data[0]['v_balance_sheet_4']
        sheet_fi = vendor_data[0]['v_balance_sheet_5']
        sheet_s = vendor_data[0]['v_balance_sheet_6']
       
        return render(request,'vendor/vendor_reg14.html',{"aadhar_reg":aadhar_reg_no,"faadhar":aadhar_father,"maadhar":aadhar_mother,"gst":gst_state,"gst_number":gst_state,"o":sheet_o,"t":sheet_t,"th":sheet_th,"f":sheet_f,"fi":sheet_fi,"s":sheet_s})
    return render(request,'vendor/vendor_reg14.html')


def Vendor_Registration_Fifteen(request):
    return render(request,'vendor/vendor_reg15.html')




def Vendor_Registration_Sixteen(request):
    if request.session.has_key('uid'):
        get_data=request.session['uid']
     
        vendor_table = VendorRegistration.objects.filter(v_email=get_data)
        
        vendor_serializer = VendorRegistration_Serializer(vendor_table,many=True)
        vendor_data = vendor_serializer.data
        mobile = vendor_data[0]['v_mobile']
        
        url = "https://www.fast2sms.com/dev/bulkV2"

        payload = "message=You are successfully register on MPMKVVCL&language=english&route=q&numbers=" +mobile
        headers = {
            'authorization': "FxOXbDJ3kKZRYH2pInuv5cigmLUWw9toEdq1zfTNSPy87heQ4AXHwf94UNnvzpjdcGmTeMZEQ0LJqYBD",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        
        # def generateOTP():
        #     digits = "0123456789"
        #     OTP = ""
        #     for i in range(6):
        #         OTP += digits[math.floor(random.random() * 10)]

        #     return OTP
        # url = "https://www.fast2sms.com/dev/bulkV2"
        # otp = generateOTP()
        # payload = "message=This is%20a%20test%20message.You are successfully register on MPMKVVCL.Your otp is "+otp+"&language=english&route=q&numbers="+str(mobile)
        
        # headers = {
        #         'authorization': "FxOXbDJ3kKZRYH2pInuv5cigmLUWw9toEdq1zfTNSPy87heQ4AXHwf94UNnvzpjdcGmTeMZEQ0LJqYBD",
        #          'Content-Type': "application/x-www-form-urlencoded",
        #          'Cache-Control': "no-cache",
        #          }    

        # response = requests.request("POST", url, data=payload, headers=headers)

        return render(request,'vendor/vendor_reg16.html')

    return render(request,'vendor/vendor_reg16.html')


def Vendor_Registration_Fifteen(request):
    return render(request,'vendor/vendor_reg15.html')

def Finance(request):
    if request.method == 'POST':
        if finance_officer.objects.filter(user_name="finance"):
            if finance_officer.objects.filter(password="12345"):
                finance = VendorRegistration.objects.all()
                finance_serializer =VendorRegistration_Serializer(finance,many=True)
                data = finance_serializer.data
                jsondata = json.loads(json.dumps(data))
                finance_data = len(jsondata)
                f_data = []
                m_data = []
                ven_name = []
                for i in range(finance_data):
                    father_data = jsondata[i]['v_upload_file_father']
                    mother_data = jsondata[i]['v_upload_file_mother']
                    vendor_data = jsondata[i]['v_company_name']
                    f_data.append(father_data)
                    m_data.append(mother_data)
                    ven_name.append(vendor_data)
                # for i in ven_name:
                #     user_data = finance_officer(v_name_of_authorized=i)
                #     user_data.save()
                print(f_data)
                lst_f_data = []
                lst_m_data = []
                for i in f_data:
                    str_i = str(i)
                    test = str_i.split('/media')
                    lst_f_data.append(test[1])
                    
                
                for i in m_data:
                    str_i = str(i)
                    test = str_i.split('/media')
                    lst_m_data.append(test[1])
                   

                final_data =zip(ven_name,f_data,m_data)
                aa = zip(ven_name,lst_f_data,lst_m_data)
                for i,j,k in aa:
                    user_data = finance_officer(v_name_of_authorized=i,v_file_upload_eleven=j,v_file_upload=k)
                    user_data.save()
                return render(request,'vendor/financedata.html',{"final":final_data}) 
                # finance_data = jsondata['v_upload_file_father']
                print(jsondata)
                # return render(request,'vendor/finance.html') 
            else:
                return render(request,'vendor/finnance_officer_sign.html')
        return render(request,'vendor/finnance_officer_sign.html')   
    return render(request,'vendor/finnance_officer_sign.html')

def Working(request):
    if request.method == 'POST':
        if working_officer.objects.filter(user_name="working"):
            if working_officer.objects.filter(password="12345"):
                finance = VendorRegistration.objects.all()
                finance_serializer =VendorRegistration_Serializer(finance,many=True)
                data = finance_serializer.data
                jsondata = json.loads(json.dumps(data))
                finance_data = len(jsondata)
                f_data = []
                m_data = []
                ven_name = []
                for i in range(finance_data):
                    father_data = jsondata[i]['v_three_years_income_1']
                    mother_data = jsondata[i]['v_three_years_income_2']
                    
                    f_data.append(father_data)
                    m_data.append(mother_data)
                   
                # for i in ven_name:
                #     user_data = finance_officer(v_name_of_authorized=i)
                #     user_data.save()
                print(f_data)
                print(m_data)
                print(ven_name)
                   

                final_data =zip(f_data,m_data)
            
                return render(request,'vendor/working_data.html',{"final_data":final_data}) 
                # finance_data = jsondata['v_upload_file_father']
                print(jsondata)
                # return render(request,'vendor/finance.html') 
            else:
                return render(request,'vendor/working_officer_sign.html')
        return render(request,'vendor/working_officer_sign.html')   
    return render(request,'vendor/working_officer_sign.html')
    
    return render(request,'vendor/working_officer_sign.html')

def mpebregiter(request):
    if request.method == 'POST':
        if officer.objects.filter(user_name="mpeb"):
            if  officer.objects.filter(password="12345"):
                finance = VendorRegistration.objects.all()
                mpeb_officer =VendorRegistration_Serializer(finance,many=True)
                data = mpeb_officer.data
                jsondata = json.loads(json.dumps(data))
                finance_data = len(jsondata)
                f_data = []
                
                for i in range(finance_data):
                    v_data = jsondata[i]['v_company_name']
                    f_data.append(v_data)              

                print("kjhkhkhellllooo",f_data)
                return render(request,'vendor/mpebdata.html',{"final":f_data}) 
                # finance_data = jsondata['v_upload_file_father']
                print(jsondata)
                # return render(request,'vendor/finance.html') 
            else:
                return render(request,'vendor/mpeb_reg.html')
        return render(request,'vendor/mpeb_reg.html')   
    return render(request,'vendor/mpeb_reg.html')