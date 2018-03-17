from django.shortcuts import render
from crud.models import Company, Laptop, Employee
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class ModelList(TemplateView):
	template_name = 'crud/model_list.html'

#Company
class CompanyCreate(CreateView):
	model = Company
	fields = ['name', 'email', 'web_page']
	success_url = reverse_lazy('company_list')

class CompanyList(ListView):
	model = Company

class CompanyDetail(DetailView):
	model = Company

class CompanyUpdate(UpdateView):
	model = Company
	fields = ['name', 'email', 'web_page']
	success_url = reverse_lazy('company_list')

class CompanyDelete(DeleteView):
	model = Company
	success_url = reverse_lazy('company_list')


#Laptop
class LaptopCreate(CreateView):
	model = Laptop
	fields = ['model', 'serial_code']
	success_url = reverse_lazy('laptop_list')

class LaptopList(ListView):
	model = Laptop

class LaptopDetail(DetailView):
	model = Laptop

class LaptopUpdate(UpdateView):
	model = Laptop
	fields = ['model', 'serial_code']
	success_url = reverse_lazy('laptop_list')

class LaptopDelete(DeleteView):
	model = Laptop
	success_url = reverse_lazy('laptop_list')

#Employee
class EmployeeCreate(CreateView):
	model = Employee
	fields = ['name', 'company', 'laptop']
	success_url = reverse_lazy('employee_list')

class EmployeeList(ListView):
	model = Employee

class EmployeeDetail(DetailView):
	model = Employee

class EmployeeUpdate(UpdateView):
	model = Employee
	fields = ['name', 'company', 'laptop']
	success_url = reverse_lazy('employee_list')

class EmployeeDelete(DeleteView):
	model = Employee
	success_url = reverse_lazy('employee_list')