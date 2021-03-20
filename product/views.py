from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .form import RegisterForm


class ProductListView(ListView):
    model = Product
    template_name = "product/product.html"
    context_object_name = "product_list"


class ProductCreateView(FormView):
    template_name = "product/register_product.html"
    form_class = RegisterForm
    success_url = "/product/"


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"

