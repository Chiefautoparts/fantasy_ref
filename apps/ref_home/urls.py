from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
	url(r'^home$', views.index, name='home'),
	url(r'^refs$', views.refs, name='refs'),
	url(r'^rules$', views.rules, name='rules'),
	url(r'^logout$', views.logout, name='logout')
]