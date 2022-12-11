from django.urls import path
from . import views
urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('add_contact/save_contact', views.save_contact, name='save_contact'),
    path('update_form/<str:pk>', views.update_form, name='update_form'),
    path('update_contact/<str:pk>',
         views.update_contact, name='update_contact'),
    path('delete_contact/<str:pk>', views.delete_contact, name='delete_contact'),
    path('pagination/<int:pk>', views.pagination, name='pagination'),
]
