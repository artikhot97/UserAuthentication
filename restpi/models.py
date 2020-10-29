# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserDetails(User):
    contact = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        db_table = 'user_details'


class EmpolyeeDetails(User):
    orgnization_name = models.CharField(max_length=200, null=True, blank=True)
    emoplye_id = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = 'empolyee_details'
