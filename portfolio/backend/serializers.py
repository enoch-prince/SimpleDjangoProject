from .models import NewUser, Employee
from rest_framework import serializers


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        #fields = '__all__'
        fields = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'last_login')
        read_only_fields = ('is_staff', 'is_active', 'is_superuser', 'last_login')


class EmployeeSerializer(serializers.ModelSerializer):
    user = NewUserSerializer()
    class Meta:
        model = Employee
        fields = ('user','type', 'profile', 'image')
        read_only_fields = ('user',)
        