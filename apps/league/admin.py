# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import League, Team, Ref, User
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
	list_display = ['team_name', 'team_location', 'owner', 'players', 'createdAt', 'updatedAt']
	list_filter = ['createdAt', 'team_name']
admin.site.register(Team, TeamAdmin)

class LeagueAdmin(admin.ModelAdmin):
	list_display = ['league_name', 'members', 'league_admin']
	list_filter = ['league_name']
admin.site.register(League, LeagueAdmin)