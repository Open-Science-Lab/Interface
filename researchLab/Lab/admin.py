from django.contrib import admin

from .models import operation,beaker,stream,operationV2

# Register your models here.

admin.site.register(operation)

admin.site.register(beaker)

admin.site.register(stream)

admin.site.register(operationV2)