from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Blog, Registeruz, Ucetnizaverka

#admin.site.register(Blog, TranslatableAdmin)
admin.site.register(Blog)
admin.site.register(Registeruz)
admin.site.register(Ucetnizaverka)
