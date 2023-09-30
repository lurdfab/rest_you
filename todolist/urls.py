from django.urls import path
from todolist.api import *


urlpatterns = [
    # path("create/", CreateTodoAPIView.as_view(), name="create"),
    # path("list/", TodoListAPIView.as_view(), name="list"),
    path("list-create/", TodoListCreateAPIView.as_view(), name="list-create"),
    path("detail/<int:id>/", TodoDetailAPIView.as_view(), name="detail"),
]
