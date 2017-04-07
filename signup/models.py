# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def publish():
    	self.save()

    def __str__(self):
        return self.email


    #def was_published_recently(self):
    #	now = timezone.now()
    #	return now - datetime.timedelta(days=1) <= self.pub_date <= now
