from django.conf.urls import url
from . import views

app_name='league'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^addTeam$', views.createTeam, name='addTeam'),
	url(r'^addLeague$', views.createLeague, name='addLeague')
]