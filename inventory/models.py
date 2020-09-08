from django.db import models
from multiuser.models import *


class CourseDetails(models.Model):
    categoryChoice = (
        ('course1', (
            ('Course 1.1', 'Course 1.1'),
            ('Course 1.2', 'Course 1.2'),
            ('Course 1.3', 'Course 1.3'),
        )),
        ('course2', (
            ('Course 2.1', 'Course 2.1'),
            ('Course 2.2', 'Course 2.2'),
        )),
        ('course3', (
            ('Course 3.1', 'Course 3.1'),
            ('Course 3.2', 'Course 3.2'),
        )),
    )
    
    statusChoice = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
        )

    belongChoice = (
        ('Trainer','Trainer'),
        ('Intitute','Institute'),
        ('Franchise','Franchise'),
        )
    id = models.AutoField(primary_key=True)
    trainer = models.ForeignKey(TrainerProfile , on_delete=models.SET_NULL ,  blank = True , null = True)
    institute = models.ForeignKey(InstituteProfile, on_delete=models.SET_NULL ,  blank = True , null = True)
    franchise = models.ForeignKey(FranchiseProfile, on_delete=models.SET_NULL ,  blank = True , null = True)
    courseName = models.CharField(max_length = 200 , null = True)
    courseDescription = models.CharField(max_length = 2000 , null = True)
    courseCategory = models.CharField(max_length = 200 , choices = categoryChoice, null=True , blank=True)
    courseOnline =  models.BooleanField(blank = True , null =True , default = False)
    courseLive =  models.BooleanField(blank = True , null =True,default = False)
    courseOffline =  models.BooleanField(blank = True , null =True,default = False)
    courseStatus = models.CharField(max_length = 30 , choices = statusChoice, null=True , blank=True)
    coursePrice =  models.DecimalField(max_digits=10,decimal_places=2)
    courseCity = models.CharField(max_length = 200 , null = True)
    courseState =  models.CharField(max_length = 200 , null = True)
    courseCountry = models.CharField(max_length = 200 , null = True,default='')
    courseBelong = models.CharField(max_length = 30 , choices = belongChoice, null=True , blank=True)
    courseAddedDate = models.DateTimeField(auto_now_add=True)
    courseVideoName= models.CharField(max_length=500,null=True , blank = True)
    courseVideoFile= models.FileField(upload_to='videos/', null=True, verbose_name="")


    def __str__(self):
        return self.courseName + " Trainer: " + self.trainer.trainerFullName

    @property
    def videoURL(self):
        try:
            url = self.courseVideoFile.url
        except:
            url = ''
        return url