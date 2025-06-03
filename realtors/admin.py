from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'is_mvp')
    list_display_links = ('id', 'name')
    list_filter = ('is_mvp', 'hire_date')
    search_fields = ('name', 'email')
    list_editable = ('is_mvp','email',)
    
    list_per_page = 25
    
admin.site.register(Realtor, RealtorAdmin)