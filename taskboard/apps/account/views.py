# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from taskboard.apps.order.models import Order
from .decorators import ValidUserMixin
from .forms import OrderCreateForm


class OrderList(ValidUserMixin, ListView):

    template_name = 'account/order_list.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(is_completed=False)


class OrderCreate(ValidUserMixin, CreateView):

    form_class = OrderCreateForm
    template_name = 'account/order_create.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        order = form.save(False)
        order.customer = self.request.user.as_customer
        return super(OrderCreate, self).form_valid(form)
