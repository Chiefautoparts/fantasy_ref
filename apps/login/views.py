# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
	# print '**INDEX**' * 500
	return render(request, 'login/index.html')

def login(request):
	# print '**LOGIN**' * 500
	results = User.objects.loginUser(request.POST)
	if results['status'] is False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('login:index')
	else:
		user = User.objects.get(id=results['user'])
		request.session['id'] = user.id
	return redirect('login:success')

def register(request):
	# print '**REGISTER**' * 500
	results = User.objects.authUser(request.POST)
	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
			return redirect('login:index')
	request.session['id'] = results['user'].id
	return redirect('login:success')

def success(request):
	# print '**SUCCESS**' * 500
	user = User.objects.get(id=request.session.get('id'))
	context = {
		'user': user
	}
	return redirect('main:home')

