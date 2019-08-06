from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Day
from .forms import DayCreateForm
from django.shortcuts import render, redirect, get_object_or_404

class IntroView(generic.TemplateView):
    template_name = 'diary/intro.html'

class IndexView(generic.ListView):
    model = Day

class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day
