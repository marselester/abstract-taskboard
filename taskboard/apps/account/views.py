# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, View
from django.shortcuts import redirect
from django.db import transaction
from django.http import Http404

from taskboard.apps.order.models import Order
from taskboard.apps.billing.models import MoneyTransfer
from .decorators import ValidUserMixin
from .forms import OrderCreateForm
from .utils import commission


class OrderList(ValidUserMixin, ListView):

    template_name = 'account/order_list.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(is_completed=False) \
                            .select_related('customer')


class OrderCreate(ValidUserMixin, CreateView):

    form_class = OrderCreateForm
    template_name = 'account/order_create.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        order = form.save(False)
        order.customer = self.request.user.as_customer
        return super(OrderCreate, self).form_valid(form)


class AcceptOrder(ValidUserMixin, View):

    @transaction.commit_on_success
    def post(self, request, *args, **kwargs):
        user = request.user

        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.select_for_update() \
                                 .exclude(customer__user=user.pk) \
                                 .get(pk=order_id, is_completed=False)
        except Order.DoesNotExist:
            raise Http404

        order.is_completed = True
        order.save()

        amount = order.cost - commission(order.cost)

        MoneyTransfer.objects.create(
            user=user,
            amount=amount,
            transfer_type=MoneyTransfer.CUSTOMER_REFILL
        )

        return redirect('order_list')
