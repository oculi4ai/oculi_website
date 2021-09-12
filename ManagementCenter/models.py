from django.db import models
from django.contrib.auth.models import User
from django.db.models import manager
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField



class ManagementCenter(models.Model):
    CEO         = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE, related_name='CEO')
    HR          = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE, related_name='HR')
    Accounter   = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE, related_name='Accounter')

class Departement(models.Model):
    name        = models.CharField(max_length=200)
    UserManager = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    name        = models.CharField(max_length=200)
    departement = models.ForeignKey(Departement,  null=True, blank=True ,on_delete=models.CASCADE)
    UserManager = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class GroupUser(models.Model):
    user        = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE)
    Group       = models.ForeignKey(Group,  null=True, blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}   ({self.Group.name})'


class GroupAdmin(models.Model):
    user        = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE)
    Group = models.ForeignKey(Group,  null=True, blank=True ,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username}   ({self.Group.name})'


class EmployerAccount(models.Model):

    genders=[
        ('Male'     , 'Male'),
        ('Female'   , 'Female')
    ]

    social_ss = [
        ('Single'   , 'Single'),
        ('Married'  , 'Married')
    ]

    user                = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE)
    first_name          = models.CharField(max_length=200)
    middle_name         = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    birth_location      = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth       = models.DateField()    
    national_number     = models.CharField(max_length=200, null=True, blank=True)
    telegram_id         = models.CharField(max_length=200, null=True, blank=True)
    phone_number        = PhoneNumberField(null=True, blank=True)
    current_address     = models.CharField(max_length=200, null=True, blank=True)
    social_status       = models.CharField(max_length=200, choices=social_ss)
    acadimec_status     = models.CharField(max_length=200)
    gender              = models.CharField(max_length=200, choices=genders)
    nationality         = CountryField()
    work_starting_date  = models.DateField()
    cv                  = models.FileField()
    
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}  ({self.user.username})'

class CustomerAccount(models.Model):
    user                = models.ForeignKey(User,  null=True, blank=True ,on_delete=models.CASCADE)
    first_name          = models.CharField(max_length=200)
    middle_name         = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    telegram_id         = models.CharField(max_length=200, null=True, blank=True)
    phone_number        = PhoneNumberField(null=True, blank=True)
