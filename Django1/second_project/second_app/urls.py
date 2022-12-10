

from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from second_app import views

urlpatterns = [
    # re_path(r'^$',views.help, name='help'),
    re_path(r'^$',views.users, name='users'),


]
