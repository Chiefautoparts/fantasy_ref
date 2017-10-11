# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ref
# Register your models here.

class RefAdmin(admin.ModelAdmin):
	list_display = ['name', 'games', 'available']
	list_filter = ['available']
admin.site.register(Ref, RefAdmin)