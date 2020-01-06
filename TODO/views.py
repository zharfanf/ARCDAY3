from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.utils import timezone
import datetime

def TodoView(request):
    all_todo_items = TodoItem.objects.all()
    timesekarang = datetime.datetime.now()
    return render(request,'todo.html', {'all_items' : all_todo_items, 'timesekarang':timesekarang})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id= todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


