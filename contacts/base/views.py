from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForm
from django.contrib import messages

# Kontaktlarni asosiy sahifada ko'rsatish


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

# Kontakt qo'shish uchun ma'lumot to'ldiriladigan sahifa


def add_contact(request):
    return render(request, 'contact_form.html')

# Kiritilgan ma'lumotni tekshirib ma'lumotlar bazasida yaratib saqlash


def save_contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        if len(phone_number) == 9 and int(phone_number):
            contact = Contact.objects.create(
                username=username, number=phone_number)
            return redirect('contacts')
        else:
            messages.add_message(
                request, messages.INFO, 'Telefon raqami 9 ta sondan iborat bo`lishi lozim')
            return redirect('add_contact')

# Tanlangan kontakning ma'lumotlarini o'zgartirish uchun sahifa


def update_form(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'update_form.html', {'contact': contact})

# O'zgartirilgan ma'lumotni tekshirib ma'lumotlar bazasida saqlash


def update_contact(request, pk):
    username = request.POST.get('username')
    phone_number = request.POST.get('phone_number')
    if len(phone_number) == 9 and int(phone_number):
        Contact.objects.filter(id=pk).update(
            username=username, number=phone_number)
        return redirect('contacts')
    else:
        messages.add_message(
            request, messages.INFO, 'Telefon raqami 9 ta sondan iborat bo`lishi lozim')
        return redirect('update_form', pk)

# Tanlangan kontakni ma'lumotlar bazasidan o'chirish


def delete_contact(request, pk):
    Contact.objects.filter(id=pk).delete()
    return redirect('contacts')
