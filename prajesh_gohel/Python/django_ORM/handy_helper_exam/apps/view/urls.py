from django.urls import path
from . import views

urlpatterns = [
    path('<id>/', views.display),
]
