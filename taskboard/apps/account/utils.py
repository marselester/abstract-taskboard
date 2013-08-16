# coding: utf-8
from __future__ import division

from django.conf import settings


def commision(amount):
    return amount * settings.ORDER_COMMISSION_RATE / 100
