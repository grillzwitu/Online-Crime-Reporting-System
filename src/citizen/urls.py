from django.urls import re_path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [

    re_path(r'^$', views.login_view , name='login'),
    re_path(r'^logout$', views.citizen_logout , name='login'),
    re_path(r'^register$', views.register_view , name='login'),
    re_path(r'^dashboard/$', views.dashboard , name='dashboard'),
    re_path(r'^create_case/$', views.create_case , name='create_case'),
    re_path(r'^cbcview/(?P<sel>\d+)/$', views.cbcview , name='cbcview'),
	re_path(r'^user_case_detail/(?P<id>\d+)/$', views.user_case_detail , name='user_case_detail'),
    re_path(r'^create_cyber_case/$', views.create_cyber_case , name='create_cyber_case'),

]
