from django.urls import path
from .import views

urlpatterns = [

    path('', views.firstapp , name="firstapp"),

    path('list', views.employee_list , name="emp_list"),
    path('form', views.employee_form , name="emp_form"),
    path('form/<int:id>/', views.employee_form , name="emp_update"),
    path('delete/<int:id>/', views.employee_delete , name="emp_delete"),
   
    path('secondapp/', views.secondapp , name="secondapp"),
]