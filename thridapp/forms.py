from django import forms
from .models import StudentOfthrid


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentOfthrid
        fields= {'stud_no','first_name','last_name','email','fields_of_study','gpa'}
       
        labels = {'stud_no':'Student_No',
                  'first_name':'First_Name',
                  'last_name':'Last_Name',
                  'email':'Email',
                  'fields_of_study':'Fields_of_Study',
                  'gpa':'GPA'}
        widgets = {'stud_no':forms.NumberInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   'fields_of_study':forms.TextInput(attrs={'class':'form-control'}),
                   'gpa':forms.NumberInput(attrs={'class':'form-control'})}