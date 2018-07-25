from django.urls import path
from . import views

urlpatterns = [
    path('<id>/', views.editpage),
    path('<id>/update/', views.update),
]
