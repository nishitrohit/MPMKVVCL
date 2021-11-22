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
    path('success' ,views.payment_success , name='success')

]
