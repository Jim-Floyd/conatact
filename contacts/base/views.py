from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator

# Kontaktlarni asosiy sahifada ko'rsatish


cont_num_in_page = 4


def contacts(request):
    # if contact_len <= cont_num_in_page:
        contacts = Contact.objects.all()
        paginator = Paginator(contacts, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'home.html', {'contacts': contacts, 'page_obj': page_obj, 'contact_len': contact_len, 'cont_num_in_page': cont_num_in_page, 'n' : range(1,page_obj.paginator.num_pages+1)})
    # return redirect('pagination', 1)







# Kontakt qo'shish uchun ma'lumot to'ldiriladigan sahifa


def add_contact(request):
    return render(request, 'contact_form.html', {'cont_num_in_page': cont_num_in_page, 'contact_len': contact_len})

# Kiritilgan ma'lumotni tekshirib ma'lumotlar bazasida yaratib saqlash
contact_len = len(Contact.objects.all())

def save_contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        if len(phone_number) == 9 and int(phone_number):
            Contact.objects.create(
                username=username, number=phone_number)
            print(contact_len)
            # if contact_len <= cont_num_in_page:
            return redirect('contacts')
            # return redirect('pagination', 1)
        else:
            messages.add_message(
                request, messages.INFO, 'Telefon raqami 9 ta sondan iborat bo`lishi lozim')
            return redirect('add_contact')


# def pagination(request, pk):
#     if contact_len % cont_num_in_page != 0:
#         all_page_num = contact_len//cont_num_in_page+1
#         if pk < all_page_num:
#             contacts_in_page = Contact.objects.all(
#             )[cont_num_in_page*(pk-1):cont_num_in_page*pk]
#         else:
#             contacts_in_page = Contact.objects.all(
#             )[cont_num_in_page*(pk-1):contact_len]
#     else:
#         all_page_num = contact_len//cont_num_in_page
#         contacts_in_page = Contact.objects.all(
#         )[cont_num_in_page*(pk-1):cont_num_in_page*pk]

    # print(all_page_num)
    # print(contact_len)
    # print(cont_num_in_page)

    # return render(request, 'home.html', {'contacts': contacts, 'contacts_in_page': contacts_in_page, 'n': range(1, all_page_num+1)})

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

def search_contact(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_contacts = Contact.objects.filter(username__contains=searched)
        return render(request, 'searched.html', {'searched_contacts': searched_contacts})

def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render(request, 'contacts', {'ctx': ctx})