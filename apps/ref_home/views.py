# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User

# Create your views here.
def index(request):
	# print '**REF_HOME**' * 250
	user = User.objects.get(id=request.session.get('id'))
	context = {
		'user': user
	}	
	return render(request, 'ref_home/index.html', context)

def refs(request):
	# print '**REFS**' * 250
	
	return render(request, 'ref_home/refs.html')

def rules(request):
	# print '**RULES**' * 250
	return render(request, 'ref_home/rules.html')

def logout(request):
    request.session.flush()
    messages.success(request, 'Logged Out')
    return redirect('login:index')
