from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^team_gen$", views.gen, name="gen"),
	url(r"^gen_data/", views.gen_data, name="gen_data"),
	url(r"^assignPlayers$", views.assignPlayers, name="assignPlayers")
]