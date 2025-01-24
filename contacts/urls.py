from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_contact, name='add_contact'),
    path('', views.contact_list, name='contact_list'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
]
