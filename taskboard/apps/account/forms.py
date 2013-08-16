# coding: utf-8
from django import forms

from taskboard.apps.order.models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('cost',)
