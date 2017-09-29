# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class RefManager(models.Manager):
	def showRefs(self, postData):
		status = {'ref': None}
		ref = Ref.objects.create(
			name = postData['name'],
			games = postData['games']
		)
		ref.save()
		status['ref'] = ref
		return status['ref']




class Ref(models.Model):
	name = models.CharField(max_length=100)
	games = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = RefManager()