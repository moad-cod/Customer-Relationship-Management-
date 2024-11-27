from django.urls import path
# from .views import (lead_detail, lead_create, lead_update, lead_delete) ==> Function Based views 
from .views import (LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView) #==> Class Based Views
app_name="leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),#always put it down {when you put it up he this think the pk is the value on bottom} or <add int:pk>
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'), 
]

