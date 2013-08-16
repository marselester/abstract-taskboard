# coding: utf-8
from django.conf.urls import patterns, url

from .views import OrderList, OrderCreate, AcceptOrder


urlpatterns = patterns('',
    url(r'^$', OrderList.as_view(), name='order_list'),
    url(r'order/add/$', OrderCreate.as_view(), name='order_add'),
    url(r'order/accept/$', AcceptOrder.as_view(), name='order_accept'),
)
