

from django.shortcuts import render , redirect
from .forms import EmployeeForm
from .models import EmployeeData

def firstapp(request):
    return render(request , 'firstapp/home.html')
def secondapp(request):
    return render(request , 'firstapp/home.html')

def employee_list(request):
    context  = {'employees':EmployeeData.objects.all()}
    return render( request ,'firstapp/employee_list.html',context)
def employee_form(request , id=0):
    if request.method == 'GET':
        if id ==0:
         form = EmployeeForm()
        else:
         employee = EmployeeData.objects.get(pk=id)
         form = EmployeeForm(instance= employee)
        return render( request ,'firstapp/employee_form.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = EmployeeData.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
        else:
         return render( request ,'firstapp/employee_form.html',{'form':form})     
def employee_delete(request,id):
    employee = EmployeeData.objects.get(pk=id)
    employee.delete()
    return redirect('emp_list')
