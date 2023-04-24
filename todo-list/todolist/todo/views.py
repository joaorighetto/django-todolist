from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


from .forms import TodoForm
from .models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'todo/todo_list.html'

    def get_queryset(self):
        return self.request.user.todo.filter(done=False)


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    success_url = '/todo'
    form_class = TodoForm

    def get_initial(self):
        return {'user': self.request.user}


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    success_url = '/todo'
    form_class = TodoForm


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/todo'
    template_name = 'todo/todo_delete.html'


def task_done(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if not task.done:
        task.done = True
        task.save()

    return redirect('todo:list')



