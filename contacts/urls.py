from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
    path('<int:contact_id>/edit/', views.edit_contact_message, name='edit_message'),
]
