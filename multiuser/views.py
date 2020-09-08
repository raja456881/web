from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from multiuser.models import AdminProfile,FranchiseProfile,InstituteProfile,TrainerProfile
from student.models import Student
from inventory.models import CourseDetails


def user(request):
    '''institute'''
    '''count'''
    institute_count=InstituteProfile.objects.all().count()

    '''apply filter'''

    all_institute=InstituteProfile.objects.all()

    '''franchise'''
    '''count'''
    franchise_count=FranchiseProfile.objects.all().count()

    '''apply filter'''
    all_franchise=FranchiseProfile.objects.all()


    '''student'''

    student_count=Student.objects.all().count()


    '''trainer'''

    trainer_count = TrainerProfile.objects.all().count()

    context={

        'trainer_count':trainer_count,
        'student_count':student_count,
        'franchise_count':franchise_count,
        'institute_count':institute_count,
        'user_count':student_count+trainer_count+franchise_count+institute_count
    }

    return render(request,'user.html',context)
