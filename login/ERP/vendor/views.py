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

def Login(request):
    if request.method == 'POST':
        if VendorRegistration.objects.filter(type=request.POST['type']):
            if VendorRegistration.objects.filter(username=request.POST['username']):
                if VendorRegistration.objects.filter(password1=request.POST['password']):
                    res = VendorRegistration.objects.filter(type=request.POST['type'],username=request.POST['username'],
                                                            password1=request.POST['password'])
                    if res:
                        request.session['uid'] = request.POST['username']
                        a= request.session['uid']
                        aa = VendorRegistration.objects.filter(username=request.session["uid"])   
                        cc = VendorRegistration_Serializer(aa,many=True)
                        dd = cc.data
                        ee = json.loads(json.dumps(dd))
                        tem = ee[-1]['temp']
                        print("helooool",tem)
                        if tem==True:
                            return redirect('dashboard')
                        else:
                            return HttpResponse("Admin not verifly your information please login after some time")
                        
                else:
                    return render(request, 'vendor/login.html', {"msg": "invalid password"})
            else:
                return render(request, 'vendor/login.html', {"msg": "invalid username"})
        else:
            return render(request, 'vendor/login.html', {"msg": "Not matched"})
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
            print("heeeeeeloo",aaaaa)
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
        print("mobile",contact)
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
            print("rraamm",get_data)
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
        print("mobile",contact)
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

# def Vendor_Registration_Six(request):
#     amount = 100 #100 here means 1 dollar,1 rupree if currency INR
#     # client = razorpay.Client(auth=(os.getenv('razorpaykey'), os.getenv('razorpaysecret')))
#     client = razorpay.Client(
#                 auth=("rzp_live_b8kvPyTH49V69F", "pl7ndE0ndRRyiYgbmH0cMyQ4"))
#     response = client.order.create({'amount':amount,'currency':'USD','payment_capture':1})
#     print(response)
#     context = {'response':response}
#     return render(request,"vendor/vendor_reg5.html",context)


# @csrf_exempt
# def payment_success(request):
#     if request.method =="POST":
#         print(request.POST)
#         return HttpResponse("Done payment hurrey!")





def Vendor_Registration_Six(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_live_b8kvPyTH49V69F", "pl7ndE0ndRRyiYgbmH0cMyQ4"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def payment_success(request):
    return render(request, "success.html")









































# error_msg = {'status':"error"}

# @api_view(['POST'])  
# def Registration(request):
#     if request.method=="POST":
#         serializers=RegistrationSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             dhd = {
#                 'status' : True,
#                 'data'  : serializers.data
#             }
            
#             return render(request,'vendor/vendor_reg1.html')
            
#         return Response(error_msg)



# @api_view(['POST'])
# def Filter(request):
#     if request.method=="POST":
#         # mobile_no = request.POST['mobile_no']
#         # food_pref = request.POST['food_pref']
#         kitchen_data = Registration()
#         mobile_no = request.query_params.get('mobile', None)
#         food_pref = request.query_params.get('food_pref', None)

#         if Registration.objects.filter(mobile=mobile_no).exists():
#             if serializers.is_valid():
#                 kitchen_data.save()
#                 return Response("Success",status=status.HTTP_201_CREATED)
#         return Response("error",status=status.HTTP_400_BAD_REQUEST)