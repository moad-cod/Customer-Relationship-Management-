from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
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
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    def form_valid(self, form):
        # send_mail(
        #     subject, #subject
        #     message, # message
        #     from_email, # from email
        #     recipient_list, # To Email
        # )
        return super(LeadCreateView, self).form_valid(form)
    
    

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:lead-list")
    

class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    
#==> functons
# def landing_page(request):
#     return render(request, 'landing.html')
# def lead_list(request):
#     Leads = Lead.objects.all()
#     context = {
#         "Leads": Leads
#     }
#     return render(request, "leads/lead_list.html", context)
# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
    
#     return render(request, "leads/lead_detail.html", context)
# def lead_create(request):
#     form = LeadModelForm() # if request.method !== "POST" form is empty
#     if request.method == "POST":
#         print("Receiving a post request") 
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save() #when we specify the model we working in (forms in LeadModelForm)
#             return redirect("/leads")
#     context= {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead) #updating instead a creating anew lead
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)      
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#      }
#     return render(request, "leads/lead_update.html", context)
# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")

