
from django.urls import re_path, include
from django.contrib import admin
from comment.views import CreateComment
from comment.views import HomePage, CommentPage
from home.views import criminal_directory
from home.views import upload_evidence
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from police.views import person_detail_view

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about$', TemplateView.as_view(template_name="about.html")),
    re_path(r'^contact', TemplateView.as_view(template_name="contact.html")),
    re_path(r'^police/', include('police.urls')),
    re_path(r'^anonymous/', include('home.url_anonymous')),
    re_path(r'^citizen/', include('citizen.urls')),
    re_path(r'comment/ajax/create', CreateComment, name = "create_comment"),
    re_path(r'comment/', CommentPage, name = "comment"),
    re_path(r'^criminal_directory/', criminal_directory, name = "criminal_directory"),
    re_path(r'evidence/(?P<id>\d+)/upload', upload_evidence, name = "upload_anonymous_evidence"),
    re_path(r'^person_detail/(?P<id>\w+)/$', person_detail_view, name='person_detail'),

    re_path(r'^$', HomePage, name = "HomePage")

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)