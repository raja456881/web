from django.db import models
from inventory.models import CourseDetails
from multiuser.models import User
from phone_field import PhoneField
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

gender=(('M','Male'),('F','Female'),('TS','Transgender'))


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_name= models.OneToOneField(User, on_delete=models.CASCADE)
    student_gender = models.CharField(choices=gender,max_length=50)
    student_profilepic = models.FileField()
    stdent_Email = models.EmailField(max_length=111)
    student_created_at = models.DateTimeField(auto_now_add=True)
    course_id = models.ForeignKey(CourseDetails, on_delete=models.DO_NOTHING, default=1)
    student_PhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    student_PhoneNo2 = PhoneNumberField(null=False, blank=False, unique=False)
    student_Street=models.CharField(max_length=250,default='')
    student_Landmark = models.CharField(max_length=100, default='')
    student_Zipcode= models.IntegerField(default='')
    student_State = models.CharField(max_length=100, default='')
    student_Country = models.CharField(max_length=100, default='')
    objects = models.Manager()

    def __str__(self):
        self.student_name -self.stdent_Email
