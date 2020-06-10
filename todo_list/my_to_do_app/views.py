from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import * 

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}

    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']

    new_todo = Todo(content=user_input_str)
    new_todo.save()

    # my_to_do_app/urls.py 내 index로 이름이 된 path로 redirect 한다.
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    todo_num = request.GET['todoNum']

    print(f'완료한 todo의 id는 {todo_num}')
    del_target_todo = Todo.objects.get(id = todo_num)
    del_target_todo.delete()

    # my_to_do_app/urls.py 내 index로 이름이 된 path로 redirect 한다.
    return HttpResponseRedirect(reverse('index'))