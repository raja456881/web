from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CourseDetailsForm ,TotalCourseForm
from .models import CourseDetails

def inventory(request):
    courseDetails = CourseDetails.objects.all()
    context = {'courseDetails':courseDetails}
    return render(request,'Trainer-inventory.html',context)

def editCourse(request,pk):
    form = CourseDetailsForm(instance = CourseDetails.objects.get(id=pk))
    context = {'form':form}
    return render(request,'inventory.html',context)

def fillcourse(request,pk):
    form = TotalCourseForm(instance=CourseDetails.objects.get(id=pk))

    courseDetails = CourseDetails.objects.all()


    context={
        'courseDetails': courseDetails,
        'form': form

         }
    return render(request,'course.html',context)


def course(request):
    '''courses'''
    '''count'''
    course_count=CourseDetails.objects.all().count()

    all_course = CourseDetails.objects.all()
    '''filter'''

    '''active_Course'''
    category_course=[]
    category_course_count = CourseDetails.objects.filter(courseCategory=category_course).count()
    c=0
    for cate in all_course:
        category_ocunt=CourseDetails.objects.filter(courseCategory=cate.courseCategory)
        c+=1

    '''category_wise'''
    active_course = []
    inactive_course = []
    a,i=0,0
    for a_ctive in all_course:
        if a_ctive.courseStatus=='active':
            a+=1
        else:
            i+=1




    context={
        'category_course_count':c,
        'course_count':course_count,
        'active_course_count':a,
        'inactive_course_count':i,


         }
    return render(request,'course.html',context)




