from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from software.models import Software

class SoftwareList(ListView):
    model = Software

class SoftwareView(DetailView):
    model = Software

class SoftwareCreate(CreateView):
    model = Software
    fields = ['company_name', 'full_name' ,'job_title','email','software_username','expiration_date','version']
    success_url = reverse_lazy('software_list')

class SoftwareUpdate(UpdateView):
    model = Software
    fields = ['company_name', 'full_name' ,'job_title','email','software_username','expiration_date','version']
    success_url = reverse_lazy('software_list')

class SoftwareDelete(DeleteView):
    model = Software
    success_url = reverse_lazy('software_list')
