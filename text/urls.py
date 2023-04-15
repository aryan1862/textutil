
from django.contrib import admin
from django.urls import path
from util1.views import index
from util1.views import length
urlpatterns = [
    path('',index,name='index'),
    path('length',length,name='length'),
]
