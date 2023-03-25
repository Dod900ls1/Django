from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['last', 'first']
