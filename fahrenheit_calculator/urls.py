from django.urls import path
from .views import get_user, get_calculator

urlpatterns = [
    path('', get_user, name="get_user"),
    path('calculator/',get_calculator, name="get_calculator"),
]
