from django.conf.urls import url
from . import views

app_name='ref'
urlpatterns = [
	url(r'^home$', views.index, name='home')
]