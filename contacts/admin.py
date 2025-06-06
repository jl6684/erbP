from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'user', 'contact_date', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing__title','phone')
    list_filter = ('contact_date', 'user')
    list_per_page = 25
    

admin.site.register(Contact, ContactAdmin)
