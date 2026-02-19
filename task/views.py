from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Count, Q
from .models import Task, Category


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.select_related('category').filter(user=self.request.user) 
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)

        cat_name = self.request.GET.get('cat')
        if cat_name:
            queryset = queryset.filter(category__name__icontains=cat_name)

        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=self.request.user).annotate(
            task_count=Count('task',
                             filter=Q(task__is_completed=False)
                            )
            )
        return context


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'category', 'is_completed']
    success_message = 'Task created successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        if 'category' in form.fields:
            form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'category', 'is_completed']
    success_message = 'Task updated successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user
    
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        if 'category' in form.fields:
            form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form
    

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-index')
    success_message = 'Task Deleted Successfully'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user
    

def about(request):
    return render(request, 'task/about.html')