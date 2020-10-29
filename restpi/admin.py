# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserDetails, EmpolyeeDetails

# Register your models here.

admin.site.register(UserDetails)
admin.site.register(EmpolyeeDetails)
