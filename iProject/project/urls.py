from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projectHome, name="projectHome"),
    path('<str:slug>', views.projectPost, name="projectPost"),
]