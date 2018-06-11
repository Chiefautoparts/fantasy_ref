# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)


class Player(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	curr_team = models.ForeignKey(Team, related_name="current_players")
	all_teams = models.ManyToManyField(Team, related_name="all_players")