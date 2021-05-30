from django.contrib import admin
from .models import Contact

class Contactadmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date', 'state' )
    list_display_links = ('id', 'name')
    search_fields =  ('id', 'name', 'listing')
    list_per_page = 25

admin.site.register(Contact, Contactadmin)

# Register your models here.
