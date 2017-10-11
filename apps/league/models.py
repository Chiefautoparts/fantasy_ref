# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from ..ref_home.models import Ref

class TeamManager(models.Manager):
	def validTeam(self, postData):
		status = { 'valid':True, 'errors': []}
		if len(postData['team_name']) < 2:
			status['valid'] = False
			status['errors'].append('Name must be more than 2 characters')
		if len(postData['team_location']) < 3:
			status['valid'] = False
			status['errors'].append('Enter a valid location more than 3 characters in lngth')
		if status['valid'] is False:
			return status

		if status['valid']:
			team = Team.objects.create(
										team_name=postData['team_name'],
										owner = User.id,
										team_location=postData['team_location'],
										players=User.Ref.name)
			team.save()
			print team.team_name


class Team(models.Model):
	team_name = models.CharField(max_length=255, default='My Team')
	owner = models.ForeignKey(User, related_name="owner")
	team_location = models.CharField(max_length=255, default='City, State')
	players = models.ForeignKey(Ref, related_name="players")
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)

	objects = TeamManager()

	def __str__(self):
		return self.team_name


class League(models.Model):
	league_name = models.CharField(max_length=255)
	members = models.ForeignKey(Team, related_name="members")
	league_admin = models.OneToOneField(User, related_name="admin")
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.league_name
