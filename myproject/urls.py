# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Giriş-çıkış view'ları için

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout sistemleri
    path('', include('employees.urls')),  # Ana sayfa çalışan listesi
]
