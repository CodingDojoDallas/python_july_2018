from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('destroy/<id>/', views.confirm),
    path('destroy/<id>/delete/', views.delete),
    path('comments/<id>/', views.comments),
    path('comments/<id>/add/', views.add),
]
