from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html')

def add_contact(request):
    return render(request, 'add_contact.html')