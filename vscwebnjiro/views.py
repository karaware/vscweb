from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ResultModel
from django.urls import reverse_lazy

class VscwebList(ListView):
    template_name = 'listnjiro.html'
    model = ResultModel
    ordering = ['-id']
    #model = ResultModel.objects.order_by('id').reverse()
    #query_set = ResultModel.objects.order_by('id').reverse()

class VscwebDetail(DetailView):
    template_name = 'detailnjiro.html'
    model = ResultModel
    
