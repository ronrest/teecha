from django.conf.urls import url
from . import views                 # import the blog views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^lesson/(?P<id>\d+)$', views.lesson, name="lesson"),
    url(r'^module/(?P<name>[a-z]{2,5}_[0-9]{1,4})$', views.module, name="module"),

]

