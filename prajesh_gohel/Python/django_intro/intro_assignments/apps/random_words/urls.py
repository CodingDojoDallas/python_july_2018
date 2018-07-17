from django.urls import path
from . import views
urlpatterns = [
    path('', views.generate),
    path('process', views.process),
    path('reset', views.reset),
]
