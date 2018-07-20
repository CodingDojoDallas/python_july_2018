from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('post/', views.post),
    path('destroy/<id>/', views.destroy),
    path('log_out/', views.log_out),
]
