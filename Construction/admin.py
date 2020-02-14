from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Client, ClientAdmin)
admin.site.unregister(Group)


class PersonInline(admin.StackedInline):
    """ Details a person in line. """
    model = Client
    can_delete = True
    verbose_name_plural = 'client'

    fields = ('username', 'email', 'city', 'province')


class UserAdmin(UserAdmin):
    inlines = [
        PersonInline
    ]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
