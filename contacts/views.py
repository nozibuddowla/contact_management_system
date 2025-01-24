from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contacts/add_contact.html", {"form": form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, "contacts/contact_detail.html", {"contact": contact})