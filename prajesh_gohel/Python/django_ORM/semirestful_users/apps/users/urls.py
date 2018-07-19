from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('new/create/', views.create),
    path('destroy/<id>', views.delete),
    path('<id>/edit/', views.edit),
    path('<id>/', views.display),
    path('<id>/edit/update/', views.update),
]
