from django import forms
from django.forms import ModelForm
from .models import Clients,Student

class ClientForm(ModelForm):
      class Meta:
            model = Clients
            fields =['name', 'email','subject', 'message']

            labels={
                  'name':'','email':'', 'subject':'', 'message':''
            }

            widgets ={
                  'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
                  'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}),
                  'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
                  'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message'})  
            }

class ApplyForm(ModelForm):
      class Meta:
            model = Student
            fields =[
                  'studentFirstName', 'studentMiddleName','studentLastName', 'studentGender',
                  'studentEmail','studentPhone','studentLevel','studentCourse','studentCountry', 'parentPhone'
                     ]
            
            labels ={
                  'studentFirstName':'', 'studentMiddleName':'','studentLastName':'', 'studentGender':'',
                  'studentEmail':'','studentPhone':'','studentLevel':'','studentCourse':'','studentUniversity':'',
                   'studentCountry':'','parentFirstNam':'','parenttLastName':'','parentEmail':'','parentPhone':''
                  }
            
            widgets ={
                  'studentFirstName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
                  'studentMiddleName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Middle Name'}),
                  'studentLastName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
                  'studentGender':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gender eg. Male or Female'}),
                  'studentEmail':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                  'studentPhone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),
                  'studentLevel':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Desired Level of study eg. Degree, Diploma or Master'}),
                  'studentCourse':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course'}),  
                  'studentCountry':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country Name'}),
                  'parentPhone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Parent Phone number'}),

            }

