
from django.contrib import admin
from django.urls import path , include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('' , include('firstapp.urls')),
    path('secondapp/' , include('secondapp.urls')),
    path('thridapp/' , include('thridapp.urls')),
   
    
]
