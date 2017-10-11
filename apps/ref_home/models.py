# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Ref(models.Model):
	name = models.CharField(max_length=200)
	games = models.IntegerField()
	available = models.BooleanField(default=True)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)