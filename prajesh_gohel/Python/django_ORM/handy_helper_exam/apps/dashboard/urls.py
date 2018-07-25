from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('destroy/<id>/', views.destroy),
    path('add/<id>/', views.add),
]
