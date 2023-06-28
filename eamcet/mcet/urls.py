from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome),
    path('form_submission/',views.form,name='form_submission'),
    path('home/',views.home,name="home"),
]