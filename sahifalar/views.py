from django.shortcuts import render
from django.views.generic import TemplateView #new


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutePageView(TemplateView):
    template_name = 'about.html'
class ProductPageView(TemplateView):
    template_name = 'product.html'
class ContactPageView(TemplateView):
    template_name = 'contact.html'