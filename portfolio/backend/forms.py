from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import NewUser, Employee

class NewUserCreationForm(UserCreationForm):
    
    class Meta:
        model = NewUser
        fields = ('email', 'first_name', 'last_name')

class NewUserChangeForm(UserChangeForm):

    class Meta:
        model = NewUser
        fields = ('email', 'first_name', 'last_name')


class EmployeeCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields= ('email', 'first_name', 'last_name')

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    type = forms.ChoiceField(choices=Employee.Types.choices)
    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.type = self.cleaned_data.get('type')
        employee.save()
        return employee
        

class EmployeeChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta(UserChangeForm.Meta):
        model = NewUser
        fields = ['email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff']
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial.get("password")