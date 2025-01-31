from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Task


class CustomloginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().filter(complete=False).count()
        return context
    
    

class Taskdetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class Taskcreate(LoginRequiredMixin,CreateView):
    model = Task
    fields ='__all__'
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model= Task
    fields ='__all__'
    success_url = reverse_lazy('tasks')
    
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model= Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
