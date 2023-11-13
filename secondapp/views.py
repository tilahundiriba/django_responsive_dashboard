from django.shortcuts import render ,redirect,get_object_or_404
from .models import Student

# Create your views here.
def home(request):
    std = Student.objects.all()
    return render(request , 'secondapp/home.html',{'std':std})
def addStudent(request):
        if request.method=='POST':
        
            std_roll = request.POST.get('roll')
            std_name = request.POST.get('name')
            std_email = request.POST.get('email')
            std_address = request.POST.get('address')
            std_phone = request.POST.get('phone')
            stds = Student()

            stds.roll = std_roll
            stds.name = std_name
            stds.email = std_email
            stds.address = std_address
            stds.phone = std_phone
            stds.save()
            return redirect('home')

        return render( request, 'secondapp/addStudent.html',{})
def delete(request,roll):
     s = Student.objects.get(pk=roll)
     s.delete()
     return redirect('home')

def update(request,roll):
    try:
        std = get_object_or_404(Student, pk=roll)
    #   std = Student.objects.get(pk=roll)
        return render(request,'secondapp/update.html',{'std':std})
    except Student.DoesNotExist:
          return render(request,'secondapp/update.html',{'message':'Student not found'})
def do_update(request ,roll):
    std_roll = request.POST.get('roll')
    std_name = request.POST.get('name')
    std_email = request.POST.get('email')
    std_address = request.POST.get('address')
    std_phone = request.POST.get('phone')

    std = Student.objects.get(pk=roll)
    std.roll = std_roll
    std.name = std_name
    std.email = std_email
    std.address = std_address
    std.phone = std_phone
    std.save()
    return redirect('home')
       