from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserChangeForm, NewUserCreationForm, EmployeeChangeForm, EmployeeCreationForm
from .models import NewUser, Employee

# Register your models here.
class NewUserAdmin(UserAdmin):
    add_form = NewUserCreationForm
    form = NewUserChangeForm
    model = NewUser
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('email', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name') }),
        ('Permissions', {'fields': ('groups','is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'reallypretty'),
            'fields': ('email', 'first_name', 'last_name','password1', 'password2', 'groups', 'is_staff', 'is_active', 'is_superuser')
        }),
    )
    search_fields = ('email', 'last_name', 'is_active')
    ordering = ('last_name', )


class EmployeeAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    list_display = ('get_email', 'get_firstname', 'get_lastname', 'type')
    list_filter = ('user', 'type')
    fieldsets = (
        (None, {'fields': ('user', 'type', ('profile', 'image'))}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('user','password1', 'password2','profile', 'image', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email', 'last_name', 'type')
    ordering = ('user', )
    filter_horizontal = ()

    def get_email(self, instance):
        return instance.user.email
    def get_firstname(self, instance):
        return instance.user.first_name
    def get_lastname(self, instance):
        return instance.user.last_name
    def get_password(self, instance):
        return instance.user.password
    def get_isstaff(self, instance):
        return instance.employee.user.is_staff
    def get_isactive(self, instance):
        return instance.user.is_active
    
    
admin.site.register(NewUser, NewUserAdmin)
admin.site.register(Employee, EmployeeAdmin)