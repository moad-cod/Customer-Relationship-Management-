from django.urls import path, include
from . import views
app_name="members"
urlpatterns = [
  path('login_user/', views.login_user, name="login"),
  path('logout_user/', views.logout_user, name="logout"),
]
