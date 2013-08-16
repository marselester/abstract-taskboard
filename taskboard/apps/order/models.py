# coding: utf-8
from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings


class Order(models.Model):

    customer = models.ForeignKey('account.Customer', related_name='orders')
    worker = models.ForeignKey('account.Worker', related_name='orders',
                               blank=True, null=True)
    cost = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(settings.MIN_ORDER_COST_RUB)])
    is_completed = models.BooleanField(default=False)
