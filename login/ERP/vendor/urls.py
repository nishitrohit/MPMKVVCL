from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import reverse
from django.views.generic.base import RedirectView

urlpatterns = [
	
	path('register', views.Registration, name='register'),
	path('login', views.Login, name='login'),
	path('vendor_registration_two', views.Vendor_Registration_Two, name='dashboard'),
	path('vendor_registration_three', views.Vendor_Registration_Three, name='dashboard2'),
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
	
	

]
