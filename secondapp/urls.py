from django.urls import path 
from .import views



urlpatterns = [

    path('home/' , views.home , name='home'),
    path('addStudent/', views.addStudent ,name="addStudent"),
    path('delete/<int:roll>/' , views.delete , name='delete'),
    path('update/<int:roll>/' , views.update , name='update'),
    path('do_update/<int:roll>/' , views.do_update , name='do_update'),
]
