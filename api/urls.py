from django.contrib import admin
from django.urls import path,include
from .views import enginePost,engineGet,getCp
urlpatterns = [
    
    
    path('enginePost/', enginePost),
    path('engineGet/', engineGet),
    path('getCp/', getCp),



]
