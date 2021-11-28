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
	path('mpeb_login', views.mbeb_login, name='mpeb_login'),
	path('home', views.vendor_home, name ="home"),

    path('vendor_base', views.vendor_base, name ="vendor_base"),
    path('vendor_material', views.vendor_material, name ="vendor_material"),
    path('vendor_purchase', views.vendor_purchase, name ="vendor_purchase"),
	path('area_base', views.area_base, name ="area_base"),
    path('area_dashboard', views.area_dashboard, name="area_dashboard"),
    path('area_process', views.area_process, name="area_process"),
    path('area_stock', views.area_stock, name="area_stock"),
    path('tkc_base', views.tkc_base, name="tkc_base"),
    path('tkc_reg', views.tkc_reg, name="tkc_reg"),	
	path('tkc_reg_two', views.tkc_reg2, name="tkc_reg2"),
	path('tkc_reg_three', views.tkc_reg3, name="tkc_reg3"),
	path('tkc_reg_four', views.tkc_reg4, name="tkc_reg4"),
	path('tkc_reg_five', views.tkc_reg5, name="tkc_reg5"),
	path('tkc_reg_six', views.tkc_reg6, name="tkc_reg6"),
	path('tkc_payment_success', views.tkc_payment_success, name="tkc_payment_success"),
	path('tkc_reg_seven', views.tkc_reg7, name="tkc_reg7"),
	path('tkc_reg_eight', views.tkc_reg8, name="tkc_reg8"),
	path('tkc_reg_nine', views.tkc_reg9, name="tkc_reg9"),
	path('tkc_reg_ten', views.tkc_reg10, name="tkc_reg10"),
	path('tkc_reg_eleven', views.tkc_reg11, name="tkc_reg11"),
	path('tkc_reg_twelve', views.tkc_reg12, name="tkc_reg12"),
	path('tkc_reg_thirtee', views.tkc_reg13, name="tkc_reg13"),
	path('tkc_reg_fourteen', views.tkc_reg14, name="tkc_reg14"),
	path('tkc_reg_fifteen', views.tkc_reg15, name="tkc_reg15"),
    path('tkc_reg_sixteen', views.tkc_reg16, name="tkc_reg16"),
	path('tkc_dash', views.tkc_dash, name="tkc_dash"),

	path('tkc_finance_login', views.Tkc_Finance_login, name='tkcfinance'),
	path('tkc_finance_home', views.Tkc_Finance, name='tkcfinance_index'),
]

