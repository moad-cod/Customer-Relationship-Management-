from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView #Class from django
from django.urls import path, include
from leads.views import LandingPageView
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('leads/', include('leads.urls', namespace='leads')),
    # path('login/', LoginView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    path('members/', include('django.contrib.auth.urls')), #Import django authentication model to use
    path('members/', include('members.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)