from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm

from .models import Order
from django.views.generic import ListView

# Create your views here.


class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            shopuser__email=self.request.session.get('user')
        )
        return queryset
