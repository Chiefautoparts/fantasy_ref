# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	print '**REF_HOME**' * 250
	return render(request, 'ref_home/index.html')