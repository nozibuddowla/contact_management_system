from django.shortcuts import render, redirect
from .forms import ContactForm

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