from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
# Create your views here.
class TaskList(ListView):
   model = Task

class TaskDetail(DetailView):
    model = Task
    template_name = 'home/task_desc.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'home/task_create.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'home/task_create.html'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'home/task_delete.html'
    success_url = reverse_lazy('tasks')