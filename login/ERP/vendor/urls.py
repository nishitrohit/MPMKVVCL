from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin

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

	path('finance_login', views.Finance, name='finance'),
	path('working_login', views.Working, name='working'),
	path('mpebregiter', views.mpebregiter, name='mpebregiter')

]
