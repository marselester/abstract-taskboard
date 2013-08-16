# coding: utf-8
from django.conf.urls import patterns, url

from .views import OrderCreate


urlpatterns = patterns('',
    url(r'order/add/$', OrderCreate.as_view(), name='order_add'),
)
