# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class MoneyTransfer(models.Model):
    """Money transfer.

    The account balance is not stored, DB stores only money transfers.
    The reason is that if user pays through payment system and he/she
    has not got enought money then they are charged first. After that
    withdrawal occurs. The result is that user does not lose money even
    if he/she can't make order.

    """

    PAYMENT_FOR_ORDER = 'payment-of-order'
    ROBOKASSA_REFILL = 'robokassa-refill'
    STRIPE_REFILL = 'stripe-refill'
    CUSTOMER_REFILL = 'customer-refill'

    TRANSFER_TYPE_CHOICES = (
        ('Withdrawal', (
            (PAYMENT_FOR_ORDER, 'Payment for an abstract order'),
        )),
        ('Refill', (
            (CUSTOMER_REFILL, 'Refill from customer'),
            (ROBOKASSA_REFILL, 'Refill through Robokassa'),
            (STRIPE_REFILL, 'Refill through Stripe'),
        )),
    )

    user = models.ForeignKey(User, related_name='money_transfers')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transfer_type = models.CharField(max_length=30,
                                     choices=TRANSFER_TYPE_CHOICES)
