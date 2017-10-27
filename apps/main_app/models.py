# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
from datetime import datetime

# Create your models here.
class Trip(models.Model):
    destination=models.CharField(max_length = 255)
    description=models.CharField(max_length = 255)
    trip_planner=models.CharField(max_length=255, default='')
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    end_date=models.DateField(auto_now=False, auto_now_add=False)
    user = models.ManyToManyField(User, related_name='traveler')
