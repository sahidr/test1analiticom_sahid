from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.user_list, name="user_list"),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail, name="user_detail"),
    url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit'),
]