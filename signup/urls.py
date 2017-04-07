from django.conf.urls import url

from . import views

app_name = 'signup'
urlpatterns = [
	#url(r'^$', views.user_list),
    url(r'^$', views.IndexView.as_view(), name='user_new'),
    url(r'^$', views.ListView.as_view(), name='user_list'),
    url(r'^$', views.DetailView.as_view(), name='user_detail'),
    #url(r'^$', views.user_list),
    #url(r'^$', views.user_detail),
]