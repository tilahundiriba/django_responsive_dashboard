from django.db import models

class StudentOfthrid(models.Model):
    stud_no = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    fields_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    def __str__(self):
        return f'{self.stud_no}{self.first_name}{self.last_name}{self.email}{self.fields_of_study}{self.gpa}'

