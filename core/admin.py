from django.contrib import admin

# Register your models here.

from .models import CrudApp

admin.site.register(CrudApp)
