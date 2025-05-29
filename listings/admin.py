from django.contrib import admin
from .models import Listing
from django.forms import NumberInput
from django.db import models

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'price', 'realtor')
    search_fields = ('title', 'description', 'address', 'price')
    list_per_page = 25
    list_editable = ('is_published', 'price')
    
    ordering = ['-id']
    
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': '10'})},
    }
    show_facets = admin.ShowFacets.ALWAYS
admin.site.register(Listing, ListingAdmin)