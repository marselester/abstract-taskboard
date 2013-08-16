# coding: utf-8
from django.db import models


class Order(models.Model):

    customer = models.ForeignKey('account.Customer', related_name='orders')
    worker = models.ForeignKey('account.Worker', related_name='orders',
                               blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)
