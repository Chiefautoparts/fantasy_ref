# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Team, Player

from . import team_generator

def gen(request):
	context = {
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "team/index.html", context)


def gen_data(request):
	team_generator.team_generate(50)
	team_generator.player_generation(200)

	return redirect('team:gen')

# Create your views here.
