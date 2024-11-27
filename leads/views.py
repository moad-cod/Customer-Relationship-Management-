from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic 
from .models import Lead, Agent
from .forms import LeadModelForm


#==>Class Based Views
# CRUD+L - Create, Retrieve, Update and Delete + List  [Detail]

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()  #ListView automatically assinged context variable into (objects_list)
    context_object_name = "leads" #use this for assigned context int a variable you want
    

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    success_url = '/leads/'

    
    def form_valid(self, form):
        print("Form data: ", form.cleaned_data)
        for field, value in form.cleaned_data.items():
            print(f"{field}: {type(value)}")
        return super().form_valid(form)
    
    

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return redirect("leads:lead-list")
    

class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return redirect("leads:lead-list")
