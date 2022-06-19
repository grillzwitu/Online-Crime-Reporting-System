from django.urls import re_path, include
from django.views.generic import TemplateView
from .views import *


urlpatterns = [

    re_path(r'^$', login_view , name='login'),
    re_path(r'^logout$', citizen_logout , name='login'),
    re_path(r'^register$', register_view , name='login'),
    re_path(r'^dashboard/$', dashboard , name='dashboard'),
    re_path(r'^create_case/$', create_case , name='create_case'),
    re_path(r'^cbcview/(?P<sel>\d+)/$', cbcview , name='cbcview'),
	re_path(r'^user_case_detail/(?P<id>\d+)/$', user_case_detail , name='user_case_detail'),
    re_path(r'^create_cyber_case/$', create_cyber_case , name='create_cyber_case'),

]
