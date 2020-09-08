from django.forms import ModelForm
from django import forms
from .models import CourseDetails

class CourseDetailsForm(forms.ModelForm):
    class Meta:
        model = CourseDetails
        fields = ['courseName','courseCategory','courseOnline','courseLive','courseOffline','courseStatus','coursePrice','courseCity','courseState','courseCountry','courseBelong']

        widgets ={
            'courseName':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-React','required':True}),
            'courseCategory':forms.Select(attrs={'class':'custom-select','required':True}),
            'courseStatus':forms.Select(attrs={'class':'custom-select','required':True}),
            'courseCity':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-Mumbai','required':True}),
            'courseState':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-Maharashtra','required':True}),
            'courseCountry':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-India','required':True}),
            'coursePrice':forms.TextInput(attrs={'class':'form-control','placeholder':'$100','required':True}),
            'courseOnline':forms.NullBooleanSelect(attrs={'class':'custom-select','required':True}),
            #'courseLive':forms.Select(attrs={'class':'custom-select','required':True}),
            'courseOffline':forms.NullBooleanSelect(attrs={'class':'custom-select','required':True}),
        }





class TotalCourseForm(forms.ModelForm):
    class Meta:
        model = CourseDetails
        fields = ['courseName', 'courseCategory', 'courseStatus', 'courseState', 'courseCountry', 'courseBelong']

        widgets = {
            'courseName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg:-React', 'required': True}),
            'courseBelong': forms.Select(attrs={'class': 'custom-select', 'required': True}),
            'courseCategory': forms.Select(attrs={'class': 'custom-select', 'required': True}),
            'courseStatus': forms.Select(attrs={'class': 'custom-select', 'required': True}),
            'courseState': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg:-Maharashtra', 'required': True}),
            'courseCountry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg:-India', 'required': True}),
              }
