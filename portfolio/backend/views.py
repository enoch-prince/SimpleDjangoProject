from rest_framework import generics
from .models import NewUser, Employee, Director, CEO
from .serializers import NewUserSerializer, EmployeeSerializer
from rest_framework.permissions import BasePermission, DjangoModelPermissions, IsAdminUser, SAFE_METHODS

class CustomUserPermission(BasePermission):
    message = "Editing someone else data is restricted to the owner and admin only"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.email == request.user.email

class CustomEmployeePermission(BasePermission):
    message = "Editing someone else data is restricted to the owner and admin only"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.user == request.user
        

class AllUsersView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer

class BasicUserCRView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = NewUser.objects.filter(is_staff=False)
    serializer_class = NewUserSerializer

class BasicUserRUDView(generics.RetrieveUpdateDestroyAPIView, CustomUserPermission):
    permission_classes = [CustomUserPermission]
    queryset = NewUser.objects.filter(is_staff=False)
    serializer_class = NewUserSerializer

class EmployeeCRView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRUDView(generics.RetrieveUpdateDestroyAPIView, CustomEmployeePermission):
    permission_classes = [CustomEmployeePermission]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DirectorCRView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser, DjangoModelPermissions]
    queryset = Director.objects.all()
    serializer_class = EmployeeSerializer

class DirectorRUDView(generics.RetrieveUpdateDestroyAPIView, CustomEmployeePermission):
    permission_classes = [CustomEmployeePermission]
    queryset = Director.objects.all()
    serializer_class = EmployeeSerializer

class CEOCRView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser, DjangoModelPermissions]
    queryset = CEO.objects.all()
    serializer_class = EmployeeSerializer

class CEORUDView(generics.RetrieveUpdateDestroyAPIView, CustomEmployeePermission):
    permission_classes = [IsAdminUser, CustomEmployeePermission]
    queryset = CEO.objects.all()
    serializer_class = EmployeeSerializer
