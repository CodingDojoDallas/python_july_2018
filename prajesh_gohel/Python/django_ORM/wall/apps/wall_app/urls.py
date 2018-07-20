from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('verify/', views.verify),
    path('wall/', views.wall),
    path('wall/post/', views.post),
    # path('wall/comment/', views.comment),
    path('log_out/', views.log_out),
]
