from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from .models import Client, Service_Provider


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


admin.site.register(Client, ClientAdmin)
admin.site.unregister(Group)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


admin.site.register(Service_Provider, ServiceAdmin)


class PersonInline(admin.StackedInline):
    """ Details a person in line. """
    model = Client, Service_Provider
    can_delete = True
    verbose_name_plural = 'client', 'service_provider'

    fields = ('username', 'email', 'city', 'province')



