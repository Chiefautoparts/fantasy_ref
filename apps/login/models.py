# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def authUser(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if not postData['first_name'] or len(postData['first_name']) < 2:
			results['status'] = False
			results['errors'].append('Invalid Name. Get it right. Everybody gets one...')
		if not postData['last_name'] or len(postData['last_name']) < 2:
			results['status'] = False
			results['errors'].append('Invalid Last Name. You\'re skating on thin ice there buck-o')
		if not postData['username'] or len(postData['username']) < 2:
			results['status'] = False
			results['errors'].append('You can come up with a better username than that.')
		if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
			results['status'] = False
			results['errors'].append('please use a real email, im not running this on Hilary Clintons server bud')
		if not postData['password'] or len(postData['password']) < 8:
			results['status'] = False
			results['errors'].append('Password is weaker than a college students feelings')
		if postData['confPassword'] != postData['password']:
			results['status'] = False
			results['errors'].append('Is it really too hard to make the two passwords match.........')
		if results['status'] is False:
			return results 

		user = User.objects.filter(username=postData['username'])

		if user:
			results['status'] = False
			results['errors'].append('Everything went horrifically wrong, run away now!!!!!!!!')

		if results['status']:
			hashpassword = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(
										first_name = postData['first_name'],
										last_name = postData['last_name'],
										username = postData['username'],
										email = postData['email'],
										password = hashpassword
										)
			user.save()
			results['user'] = user
		return results

	def loginUser(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		user = User.objects.filter(username=postData['username'])

		try:
			user
		except IndexError:
			results['status'] = False
			results['errors'].append('OH GOD NO ITS FAILING.... call I.T. NOW!!!!')

		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
				results['status'] = False
				results['errors'].append('Username or Password are invalid. notifing authorities on your location')
			else:
				results['user'] = user[0].id
		else:
			results['status'] = False
		return results

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
