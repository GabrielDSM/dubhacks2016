from django.contrib import admin
# Register your models here.

from .models import PersonEntry, Major

admin.site.register(PersonEntry)
admin.site.register(Major)
