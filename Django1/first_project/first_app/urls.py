

from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    re_path(r'^$',views.index, name='index'),

]
