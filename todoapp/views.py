from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

def index(request):
    todoItems = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todoItems': todoItems, 'form': form}
    return render(request,'todoapp/index.html', context)

@require_POST
def addItem(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_item = Todo(text=request.POST['text'])
        new_item.save()

    return redirect('index')

def completedItem(request, todoId):
    todo = Todo.objects.get(pk=todoId)
    todo.completed = True
    todo.save()
    #print(todo.completed)
    return redirect('index')

def uncheckCompleted(request, todoId):
    todo = Todo.objects.get(pk=todoId)
    todo.completed = False
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')