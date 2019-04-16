'''
Created on 22 de mar de 2019

@author: filiped
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_01, name='index1'),
    path('<str:token>/', views.index, name='index'),
    
]