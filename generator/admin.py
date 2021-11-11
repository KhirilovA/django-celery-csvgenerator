from django.contrib import admin
from .models import Scheme

@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    view_on_site = True
