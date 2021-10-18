from django.urls import path
from .views import add_todo,todos,delete_todo
urlpatterns = [
    path('', todos, name="todos"),
    path('addTodo/',add_todo,name="add_todo"),
    path('deleteTodo/<int:id>',delete_todo,name="delete_todo")
]