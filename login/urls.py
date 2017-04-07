from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.get_queryset, name='user'),
    #url(r'^$', views.IndexView.as_view(), name='user_new'),
   
]