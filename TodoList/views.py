from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
import datetime
from .models import Todo


def listing(request):
    context = {
        "Todo":Todo.getOrderByPriority(),
        "today":datetime.date.today(),
        "len_pri1":Todo.objects.filter(priority=1).count(),
        "len_pri2":Todo.objects.filter(priority=2).count(),
        "len_pri3":Todo.objects.filter(priority=3).count(),
        "overdue":Todo.getOverDueNotFinished(),
    }
    return render(request,"TodoList/list.html", context)
    
def add(request):
    arg = ['name','body','priority','due','csrfmiddlewaretoken']
    post = request.POST
    if len(arg^post.keys())!=0 or post['name']=='':
        print(post)
        return HttpResponseRedirect(reverse('list'))
        
    due = datetime.date(*list(map(int,post['due'].split('-')))) if post['due']!='' else None
    newTodo = Todo(name=post['name'], body=post['body'], due=due,
        priority=post['priority'])
    newTodo.save()
    return HttpResponseRedirect(reverse('list'))

def modify(request):
    arg = ['id', 'name','body','priority','due','csrfmiddlewaretoken']
    post = request.POST
    if len(arg^post.keys())!=0 or post['name']=='':
        print(post)
        return HttpResponseRedirect(reverse('list'))

    todo = get_object_or_404(Todo,pk=int(post['id']))
    due = datetime.date(*list(map(int,post['due'].split('-')))) if post['due']!='' else None
    
    todo.name, todo.body, todo.due, todo.priority =  \
        post['name'], post['body'], due, post['priority']
    todo.save()
    return HttpResponseRedirect(reverse('list'))

def remove(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return HttpResponseRedirect(reverse('list'))

def toggle(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.finish = not todo.finish
    todo.save()
    return HttpResponseRedirect(reverse('list'))

def mod_priority(request,id):
    todo = get_object_or_404(Todo, pk=id)
    todo.priority = todo.priority-1 if todo.priority>1 else 3
    todo.save()
    return HttpResponseRedirect(reverse('list'))