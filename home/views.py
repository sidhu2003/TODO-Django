from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
# Create your views here.
class TaskList(ListView):
   model = Task

class TaskDetail(DetailView):
    model = Task
    template_name = 'home/task_desc.html'