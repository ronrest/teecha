from django.conf.urls import url
from . import views                 # import the blog views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^lesson/(?P<id>\d+)$', views.lesson, name="lesson"),
    url(r'^module/(?P<id>\d+)$', views.module, name="module"),

]

