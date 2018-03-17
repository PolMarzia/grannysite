from mainsite.views import *
from django.conf.urls import url
from mainsite import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$', views.mainpage, name='index'),
    url(r'^main/$', views.mainpage, name='index'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)