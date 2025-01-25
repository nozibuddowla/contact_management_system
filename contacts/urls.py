from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_contact, name="add_contact"),
    path("", views.contact_list, name="contact_list"),
    path("contacts/<int:pk>/", views.contact_detail, name="contact_detail"),
    path("contacts/edit/<int:pk>/", views.edit_contact, name="edit_contact"),
    path("contacts/delete/<int:pk>/", views.delete_contact, name="delete_contact"),
]
