from django.urls import re_path, include
from django.views.generic import TemplateView
from .views import *
urlpatterns = [

 re_path(r'^$', login_view , name='login'),
 re_path(r'^dashboard/$', dashboard , name='police_dashboard'),
 re_path(r'^logout/$', police_logout , name='police_logout'),

 re_path(r'^cbc/(?P<id>\d+)/$', cbcview , name='cbc'),
 re_path(r'^cybercbc/(?P<id>\d+)/$', cybercbcview , name='cybercbc'),


 re_path(r'^ajax/get_category/', get_case_categories, name = "get_categories"),

 re_path(r'^case_detail/(?P<id>\d+)/(?P<approved>\d+)/$', case_detail , name='case_detail'),

 re_path(r'^create_criminal_details/$', create_criminal_details , name='create_criminal_details'),

 re_path(r'^atips/$', atips , name='atips'),
 re_path(r'^atip_detail/(?P<id>\d+)/$', atip_detail, name='atip_detail'),


]
