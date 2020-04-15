
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hr.urls')),
    path('',include('manage_auth.urls')),
]
