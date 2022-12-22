from django.urls import include, re_path
# from django.conf.urls import url
from basic_app import views

app_name='basic_app'
urlpatterns = [
    re_path(r'^$',views.SchoolListView.as_view(),name='list'),
    re_path(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    re_path(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
    re_path(r'^update(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    re_path(r'^delete(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete')



]
    # path("admin/", admin.site.urls),
    # # Calling Class based views
    # # re_path(r'^$', views.CBView.as_view())
    # re_path(r'^$', views.IndexView.as_view()),
    # re_path(r'^basic_app/',include('basic_app.urls',namespace='basic_app'))




    # re_path(r'^basic_app/', include('basic_app.urls')),
    # re_path(r'^logout/$', views.user_logout, name='logout'),
    # re_path(r'special/', views.special, name='special')
