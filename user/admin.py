from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

def make_desactive(modeladmin, news, queryset):
    queryset.update(is_active=False)
    make_desactive.short_description = u"desactivate selected Users"

def make_active(modeladmin, news, queryset):
    queryset.update(is_active=True)
    make_active.short_description = u"desactivate selected Users"

def reset_ref(modeladmin, news, queryset):
    queryset.update(recommended_by="")
    make_active.short_description = u"reset selected Users"


class CustomUserAdmin(UserAdmin):
    actions = [make_desactive,make_active]


class SettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'code','recommended_by')
    actions = [reset_ref]

class SettingContact(admin.ModelAdmin):
    list_display = ('title', 'user')


class Settinguser(admin.ModelAdmin):
    list_display = ('usernam', 'password','ipCountry')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Anonnce)
admin.site.register(contact,SettingContact)
admin.site.register(profile,SettingAdmin)
admin.site.register(UserPass,Settinguser)





# Register your models here.
