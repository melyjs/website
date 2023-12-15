from django.contrib import admin

# Register your models here.

from django.contrib.admin import ModelAdmin

from .models import Cursos

# Register your models here.

@admin.register(Cursos)
class CursosAdmin(ModelAdmin):
    ...