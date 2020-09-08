
from django.db import models
from phone_field import PhoneField
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_institute = models.BooleanField(default=False)
    is_franchise = models.BooleanField(default=False)

class AdminProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='admin')
    adminFullName = models.CharField(max_length=150 , blank=True)
    adminEmail = models.EmailField(max_length = 100 , blank = True)
    adminPhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    adminPhoneNo2 = PhoneNumberField(null=False, blank=False, unique=False)
    adminAddress = models.CharField(max_length= 500 , blank = True)
    adminState = models.CharField(blank=True,max_length=50)
    adminCountry = models.CharField(max_length=20,blank=False,default='')
    adminAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.adminFullName

class TrainerProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='trainer')
    trainerFullName = models.CharField(max_length=150 , blank=True)
    trainerEmail = models.EmailField(max_length = 100 , blank = True)
    trainerPhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    trainerPhoneNo2 = PhoneNumberField(null=False, blank=False, unique=False)
    trainerAddress = models.CharField(max_length= 500 , blank = True)
    trainerState = models.CharField(blank=True,max_length=50)
    trainerCountry = models.CharField(max_length=20,blank=False,default='')
    trainerAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.trainerFullName

class InstituteProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='institute')
    instituteName = models.CharField(max_length = 200 , blank = True)
    instituteEmail = models.EmailField(max_length = 100 , blank = True)
    institutePhoneNo1 = PhoneNumberField(null=True, blank=True, unique=False)
    institutePhoneNo2 = PhoneNumberField(null=True, blank=True, unique=False)
    instituteAddress = models.CharField(max_length= 500 , blank = True)
    intituteState = models.CharField(blank=True,max_length=50)
    instituteCountry = models.CharField(max_length=20,blank=False,default='')
    instituteAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.instituteName

class FranchiseProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='franchise')
    franchiseName = models.CharField(max_length = 200 , blank = True)
    franchiseEmail = models.EmailField(max_length =100 , blank = True)
    franchisePhoneNo1 = PhoneNumberField(null=True, blank=True, unique=False)
    franchisePhoneNo2 = PhoneNumberField(null=True, blank=True, unique=False)
    franchiseAddress = models.CharField(max_length= 500 , blank = True)
    franchiseState = models.CharField(blank=True,max_length=50)
    franchiseCountry = models.CharField(max_length=20,blank=False,default='')
    franchiseAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.franchiseName


