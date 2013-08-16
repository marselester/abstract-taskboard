# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .decorators import ValidUserMixin
from .forms import OrderCreateForm


class OrderCreate(ValidUserMixin, CreateView):

    form_class = OrderCreateForm
    template_name = 'account/order_create.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        order = form.save(False)
        order.customer = self.request.user.as_customer
        return super(OrderCreate, self).form_valid(form)
