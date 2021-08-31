from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']

# Register your models here.
admin.site.register(zearch,PostAdmin)