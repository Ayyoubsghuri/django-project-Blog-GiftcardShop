from django.contrib import admin
from .models import *


# class PostAdmin(admin.ModelAdmin):
# # Register your models here.
#     prepopulated_fields = {'listacc()': ('acc',)}
class PostAdmin(admin.ModelAdmin):
    list_display = ('acc', 'title', 'user')



admin.site.register(shopp)
admin.site.register(shoporder,PostAdmin)

