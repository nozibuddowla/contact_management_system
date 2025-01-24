from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact

# Create your views here.
# Add Contact
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contacts/add_contact.html", {"form": form})

# View Contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

# Contact Detail
def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, "contacts/contact_detail.html", {"contact": contact})

# Edit Contact
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
        
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/edit_contact.html", {"form": form})

# Delete Contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/delete_contact.html", {"contact": contact})