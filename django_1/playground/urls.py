from django.urls import path
from . import views 

#URL CONFIG

urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('form/', views.show_form, name='form'),
]