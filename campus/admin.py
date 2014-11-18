from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from campus.models import *



class MyUserAdmin(UserAdmin):

    list_display = ("username","first_name", "last_name", "email","is_active","is_staff","last_login","date_joined")

    ## Static overriding 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'user_permissions','groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


    def get_form(self, request, obj=None, **kwargs):
        
        if not request.user.is_superuser: 
            self.exclude = ("user_permissions",)
            self.fieldsets[2][1]["fields"] = ('is_active','groups')

        form = super(MyUserAdmin,self).get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        qs = super(MyUserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(is_staff=False)
        return qs

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(Estudiante)
admin.site.register(Formador)
admin.site.register(Clases)
admin.site.register(Cursos)
admin.site.register(Actividad)