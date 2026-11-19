from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('administration/', views.admin_page, name='admin_page'),
    path('contact/', views.contact, name='contact'),
]