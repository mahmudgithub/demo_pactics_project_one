#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from .models import City


class HomePageView(ListView):
    model = City
    template_name = 'home.html'
    context_object_name='sok'

