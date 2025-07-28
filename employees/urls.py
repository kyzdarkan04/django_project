# employees/urls.py
from django.urls import path
from . import views
from .views import signup_view

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('signup/', signup_view, name='signup'),
]
