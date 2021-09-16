from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ResultModel
from django.urls import reverse_lazy

class VscwebList(ListView):
    template_name = 'listpekora.html'
    model = ResultModel
    ordering = ['-id']

class VscwebDetail(DetailView):
    template_name = 'detailpekora.html'
    model = ResultModel
