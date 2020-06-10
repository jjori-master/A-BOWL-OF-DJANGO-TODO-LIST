from django.urls import path
from . import views

# path에 name을 입력해주는 이유는
# redirect시 각 path로 매핑 시켜줄때
# url을 적는 대신 name을 이용하여 접근할 수 있도록 하기 위함.
urlpatterns = [
    path('', views.index, name="index"),
    path('createTodo/',  views.createTodo, name='createTodo'),
    path('deleteTodo/',  views.deleteTodo, name='deleteTodo')
]