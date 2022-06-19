from django.urls import re_path, include
from django.views.generic import TemplateView
from .views import anonymous_tip, anonymous_user_login, anonymous_dashboard, get_interact_anonymous

urlpatterns = [

    re_path(r'^$', anonymous_tip, name='anonymous_tip'),
    re_path(r'^login$', anonymous_user_login, name='anonymous_user_login'),
    re_path(r'^dashboard$', anonymous_dashboard, name="anonymous_dashboard"),
]
