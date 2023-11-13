from django.db import models



class Position(models.Model):
     title = models.CharField(max_length=500)
     def __str__(self):
           return f'{self.title}'

# Create your models here.
class EmployeeData(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey( Position , on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.fullname} {self.emp_code} {self.mobile} {self.position} {self.position.title}'
    