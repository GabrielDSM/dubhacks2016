from django.contrib import admin

# Register your models here.

from .models import Woman, Major

admin.site.register(Woman)
admin.site.register(Major)
