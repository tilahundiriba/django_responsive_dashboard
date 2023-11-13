

from django.shortcuts import render ,redirect
from .models import StudentOfthrid
from .forms import StudentForm
def home(request):
    students = StudentOfthrid.objects.all()
    return render(request , 'thridapp/home.html', {'students':students})
def views_student(request , id):
    student = StudentOfthrid.objects.get(pk=id)
    return redirect('home')
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            n_std_no = form.cleaned_data['stud_no']
            n_std_fname = form.cleaned_data['first_name']
            n_std_lname = form.cleaned_data['last_name']
            n_std_email = form.cleaned_data['email']
            n_std_fstudy = form.cleaned_data['fields_of_study']
            n_std_gpa = form.cleaned_data['gpa']
            new_student=StudentOfthrid(
              stud_no =  n_std_no, 
              first_name =  n_std_fname, 
              last_name =  n_std_lname, 
              email =  n_std_email, 
              fields_of_study =  n_std_fstudy, 
              gpa =  n_std_gpa 

            )
            new_student.save()
            return render(request , 'thridapp/add.html', {
                'form':StudentForm(),
                  'success':True    
                  })
    else:
        form = StudentForm()
        return render(request , 'thridapp/add.html',
        { 'form':StudentForm()})
    
def edit(request , id):
   if request.method == "POST":
        student = StudentOfthrid.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
          form.save()
          return  render(request,'thridapp/edit.html',{
            'form':form,
            'success':True
        })
   else:
       student  =StudentOfthrid.objects.get(pk=id)
       form = StudentForm(instance=student)
   return render(request , 'thridapp/edit.html',
                 {'form':form})
def delete(request, id):
    if request.method == 'POST':
        student = StudentOfthrid.objects.get(pk=id)
        student.delete()
    return redirect('home')
       