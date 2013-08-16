# coding: utf-8
from __future__ import division
from decimal import Decimal

from django.conf import settings


def commission(amount):
    result = amount * Decimal(settings.ORDER_COMMISSION_RATE) / Decimal('100')
    return result.quantize(Decimal('0.01'))
