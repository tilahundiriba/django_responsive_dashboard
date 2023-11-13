from django.urls import path , include
from .import views

urlpatterns = [

    path('home/',views.home , name="home"),
    path('<int:id>',views.views_student , name="views_student"),
    path('add/',views.add , name="add"),
    path('edit/<int:id>/',views.edit , name="edit"),
    path('delete/<int:id>/' , views.delete , name="delete")
    
]
