from django.contrib import admin

# Register your models here.
from  .models import Listing

class ListingAdmin (admin.ModelAdmin):
    list_display = ('id','title','is_publish','price','list_date', 'realtor')
    list_display_links =  ('id','title')
    list_filter = ('realtor__name',)
    list_editable = ('is_publish', )
    search_fields = ('title', 'description','city','adress','state')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)