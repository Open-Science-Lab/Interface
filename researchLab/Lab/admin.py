from django.contrib import admin

from .models import operation,beaker,stream

# Register your models here.

admin.site.register(operation)

admin.site.register(beaker)

admin.site.register(stream)