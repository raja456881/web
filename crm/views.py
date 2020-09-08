from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from multiuser.models import FranchiseProfile,InstituteProfile,TrainerProfile
from student.models import Student
from django.conf import settings
from easy_pdf.views import PDFTemplateView
from .models import location1
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice
from.pdf import draw_pdf
from .apps import pdf_response


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


from django.contrib import messages
def BulckEmail(request):
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']

        print(name)
        if name=='Student':
            print(name)
            for user in Student.objects.all():
                recivers_list.append(user.stdent_Email)
        elif name=='Trainer':
            print(name)
            for user in TrainerProfile.objects.all():
                recivers_list.append(user.trainerEmail)
        elif name=='Institution':
            print(name)
            for user in InstituteProfile.objects.all():
                recivers_list.append(user.instituteEmail)
        elif name=='Franchise':
            print(name)
            for user in FranchiseProfile.objects.all():
                recivers_list.append(user.franchiseEmail)
        email1=mail.EmailMessage( subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return render(request, "bulk-mail.html")




def studentsingeemail(request):
    student=Student.objects.all()
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name)
        recivers_list.append(name)
        print(name)
        email1=mail.EmailMessage(subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return render(request , "individual-mail.html", {'context': student})
def trainersingeemail(request):
    Trainer1=TrainerProfile.objects.all()
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        recivers_list.append(name)
        email1=mail.EmailMessage(subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
        message.success(request, "sucessful send mail")
    return  render(request, "individual-mail.html", {'context': Trainer1})


def Institutionsingeemail(request):
    institution=InstituteProfile.objects.all()
    if request.method=='POST':
        from django.core import mail
        connection=mail.get_connection()
        connection.open()
        recivers_list=[]
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        recivers_list.append(name)
        email1=mail.EmailMessage(subject, message , 'rajasaini12345641@gmail.com', recivers_list, connection=connection)
        email1.send()
        connection.close()
    return  render(request, "individual-mail.html", {'context': institution})


def location(request):
    if request.method=='POST':
        country1=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        locat=location1(country=country1, state=state, city=city)
        locat.save()
        return render(request, 'locat.html')

    return render(request, 'locat.html')

class HelloPDFView(PDFTemplateView):
    template_name = 'hello.html'

    base_url = 'file://' + settings.MEDIA_ROOT
    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            **kwargs
        )




def pdf_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)


@login_required
def pdf_user_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id, user=request.user)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)
