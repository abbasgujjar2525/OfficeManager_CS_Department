
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('pages.urls')),
    path('complaints/', include('Complaints.urls')),
    path('applications/', include('Applications.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
