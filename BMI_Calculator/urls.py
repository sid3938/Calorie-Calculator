from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.BMI_home, name='BMI_home'),
]
