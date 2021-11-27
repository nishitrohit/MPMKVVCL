from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import reverse
from django.views.generic.base import RedirectView

urlpatterns = [

	path('login', views.Login, name='login'),
	path('register', views.Registration, name='register'),
	path('vendor_registration_two', views.Vendor_Registration_Two, name='dashboard'),
	path('vendor_registration_three', views.Vendor_Registration_Three, name='dashboard2'),

	path('otp', views.otp , name='otp'),

	path('vendor_registration_four', views.Vendor_Registration_Four, name='dashboard3'),
	path('vendor_registration_five', views.Vendor_Registration_Five, name='dashboard4'),
	# path('payment/', views.Vendor_Registration_Six, name='payment/'),
	
	# path('success/',views.payment_success, name='payment-success'),

	path('vendor_registration_six',views.Vendor_Registration_Six, name='home'),
    path('success' ,views.payment_success , name='success'),
    path('vendor_registration_seven', views.Vendor_Registration_Seven, name='dashboard5'),
	path('vendor_registration_eight', views.Vendor_Registration_Eight, name='dashboard6'),
	path('vendor_registration_nine', views.Vendor_Registration_Nine, name='dashboard7'),
	path('vendor_registration_ten', views.Vendor_Registration_Ten, name='dashboard8'),
	path('vendor_registration_eleven', views.Vendor_Registration_Eleven, name='dashboard9'),

	path('vendor_registration_twelve', views.Vendor_Registration_Twelve, name='dashboard10'),
	path('vendor_registration_thirteen', views.Vendor_Registration_Thirteen, name='dashboard11'),
	path('vendor_registration_fourteen', views.Vendor_Registration_Fourteen, name='dashboard12'),
	path('vendor_registration_fifteen', views.Vendor_Registration_Fifteen, name='dashboard13'),
	path('vendor_registration_sixteen', views.Vendor_Registration_Sixteen, name='dashboard14'),

	path('finance_login', views.Finance_login, name='finance'),
	path('finance_home', views.Finance, name='finance_index'),
	path('working_login', views.Working, name='working'),
	path('mpebregiter', views.mpebregiter, name='mpebregiter'),

	path('home', views.vendor_home, name ="home"),
    path('vendor_base', views.vendor_base, name ="vendor_base"),
    path('vendor_material', views.vendor_material, name ="vendor_material"),
    path('vendor_purchase', views.vendor_purchase, name ="vendor_purchase"),
    
    path('area_base', views.area_base, name ="area_base"),
    path('area_dashboard', views.area_dashboard, name="area_dashboard"),
    path('area_process', views.area_process, name="area_process"),
    path('area_stock', views.area_stock, name="area_stock"),
    
    path('procurement_base', views.procurement_base, name ="procurement_base"),
    path('procurement_dashboard', views.procurement_dashboard, name="procurement_dashboard"),
    path('procurement_previous_po', views.procurement_previous_po, name="procurement_previous_po"),
	path('procurement_generate_po', views.procurement_generate_po, name="procurement_generate_po"),	


	path('nabl_register', views.nabl_Registration, name='nabl_register'),

	path('nabl_otp', views.nabl_otp , name='nabl_otp'),

	path('nabl_Registration_two', views.nabl_Registration_Two, name='nabl_dashboard'),
	path('nabl_Registration_three', views.nabl_Registration_Three, name='nabl_dashboard2'),
	path('nabl_Registration_four', views.nabl_Registration_Four, name='nabl_dashboard3'),
	path('nabl_Registration_five', views.nabl_Registration_Five, name='nabl_dashboard4'),
	path('nabl_Registration_six', views.nabl_Registration_Six, name='nabl_dashboard5'),
	path('nabl_Registration_seven', views.nabl_Registration_Seven, name='nabl_dashboard6'),
	path('nabl_Registration_eight', views.nabl_Registration_Eight, name='nabl_dashboard7'),
	path('nabl_Registration_nine', views.nabl_Registration_Nine, name='nabl_dashboard8'),



]
