from django.urls import path
from food.views import *
app_name='tasty'
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani')
]