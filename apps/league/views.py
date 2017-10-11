# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Team, League, Ref, User
# Create your views here.


def home(request):
	print '**LEagueHOME**' * 250

def createTeam(request):
	print '**createTeam**' * 250

def createLeague(request):
	print '**add league**' * 250