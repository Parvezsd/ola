from django.urls import path
from shopping.views import *
app_name='new'
urlpatterns=[
    path('car/',car,name='car'),
]