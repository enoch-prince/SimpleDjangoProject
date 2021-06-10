from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import AccountManager, DirectorManager, CEOManager

# Create your models here.
class NewUser(AbstractBaseUser, PermissionsMixin):
    objects = AccountManager()

    email = models.EmailField(_("Email"), max_length=80, null=False, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50, null=False)
    last_name = models.CharField(_("Surname"), max_length=50, null=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Employee(models.Model):

    class Types(models.TextChoices):
        '''Python version of an enum class '''
        EMPLOYEE = "EMPLOYEE", "Employee"
        DIRECTOR = "DIRECTOR", "Director"
        CEO = "CEO", "CEO"
    
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(_("Type of User"),max_length=20, choices=Types.choices, default=Types.EMPLOYEE)
    profile = models.TextField(_("About Info"), blank=True)
    image = models.ImageField(_("Profile Picture"), upload_to='uploads/', blank=True)

    
    #objects = EmployeeManager()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            '''If the record does not exist, the user will have the Director type '''
            #self.type = self.Types.EMPLOYEE
            self.is_staff = True
        return super().save(*args, **kwargs)

class Director(Employee):
    objects = DirectorManager()
    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            '''If the record does not exist, the user will have the Director type '''
            self.type = self.Types.DIRECTOR
            #self.is_staff = True
        return super().save(*args, **kwargs)

class CEO(Employee):
    objects = CEOManager()
    
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            '''If the record does not exist, the user will have the CEO type '''
            self.type = self.Types.CEO
            #self.is_staff = True
        return super().save(*args, **kwargs)


############# Login Details #############
# admin@example.com | admin
# fo@company.com | RNvUhJr4JtvqE9s
# jasonsmith@anydomian.com| xwpG4BcjYD6QNpb
