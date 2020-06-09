from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import * 

# Create your views here.
def index(request):
    return render(request, 'my_to_do_app/index.html')

def createTodo(request):
    user_input_str = request.POST['todoContent']

    new_todo = Todo(content=user_input_str)
    new_todo.save()

    # my_to_do_app/urls.py 내 index로 이름이 된 path로 redirect 한다.
    return HttpResponseRedirect(reverse('index'))