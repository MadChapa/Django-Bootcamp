from django.urls import include, re_path
# from django.conf.urls import url
from basic_app import views


# template tagging
app_name='basic_app'
urlpatterns=[
    re_path(r'^relative/$', views.relative, name='relative'),
    re_path(r'^other/$', views.other, name='other'),

]
