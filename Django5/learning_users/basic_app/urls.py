from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from basic_app import views

# TEMPLATE URLs
app_name='basic_app'
urlpatterns = [
    # Register View
    re_path(r'^register/$',views.register, name='register'),
     #Login Views
     re_path(r'^user_login/$',views.user_login, name='user_login'),

]
