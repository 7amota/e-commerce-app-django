from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *

class IndexViews(ListView):
    model = Product
    template_name = 'pages/index.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('?')
        context['pwd']= Product.objects.filter(price_with_discount__lte=25)
        return context
