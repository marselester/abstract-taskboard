# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    user = models.OneToOneField(User, related_name='as_customer')


class Worker(models.Model):

    user = models.OneToOneField(User, related_name='as_worker')
