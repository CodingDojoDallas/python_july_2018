from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('verify/', views.verify),
    path('user/<id>/', views.display),
    path('myaccount/<id>/', views.edit),
    path('myaccount/<id>/update/', views.update),
]
