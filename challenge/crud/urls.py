from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ModelList.as_view(), name='model_list'),
	url(r'^company/create$', views.CompanyCreate.as_view(), name='company_create'),
	url(r'^company$', views.CompanyList.as_view(), name='company_list'),
	url(r'^company/detail/(?P<pk>\d+)/$', views.CompanyDetail.as_view(), name='company_detail'),
	url(r'^company/update/(?P<pk>\d+)/$', views.CompanyUpdate.as_view(), name='company_update'),
	url(r'^company/delete/(?P<pk>\d+)/$', views.CompanyDelete.as_view(), name='company_delete'),
	url(r'^laptop/create$', views.LaptopCreate.as_view(), name='laptop_create'),
	url(r'^laptop$', views.LaptopList.as_view(), name='laptop_list'),
	url(r'^laptop/detail/(?P<pk>\d+)/$', views.LaptopDetail.as_view(), name='laptop_detail'),
	url(r'^laptop/update/(?P<pk>\d+)/$', views.LaptopUpdate.as_view(), name='laptop_update'),
	url(r'^laptop/delete/(?P<pk>\d+)/$', views.LaptopDelete.as_view(), name='laptop_delete'),
	url(r'^employee/create$', views.EmployeeCreate.as_view(), name='employee_create'),
	url(r'^employee$', views.EmployeeList.as_view(), name='employee_list'),
	url(r'^employee/detail/(?P<pk>\d+)/$', views.EmployeeDetail.as_view(), name='employee_detail'),
	url(r'^employee/update/(?P<pk>\d+)/$', views.EmployeeUpdate.as_view(), name='employee_update'),
	url(r'^employee/delete/(?P<pk>\d+)/$', views.EmployeeDelete.as_view(), name='employee_delete'),
]
