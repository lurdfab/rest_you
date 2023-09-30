from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todolist.serializers import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from todolist.pagination import CustomPageNumberPagination


#this class below does the same thing the create & list class does but in a single class

class TodoListCreateAPIView(ListCreateAPIView):
    
        serializer_class = TodoSerializer
        pagination_class = CustomPageNumberPagination
        permission_classes = (IsAuthenticated,)#we want the user to be authenticated before creating a todo
        filter_backends = (DjangoFilterBackend, filters.SearchFilter)#we want to use the django filter backend
        filterset_fields = ("is_completed", "id", "title")#we want to filter the todos based on the fields in the list
        search_fields = ("is_completed", "id", "title") #we want to search the todos based on the fields in the list
    
        def get_queryset(self):
            return Todo.objects.filter(owner=self.request.user) #we want the owner of the todo to be the user that created it
    
        def perform_create(self, serializer):
            return serializer.save(owner=self.request.user) #we want the owner of the todo to be the user that created it
        


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)#we want the user to be authenticated before creating a todo
    lookup_field = "id" #we want to use the id to get the todo

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user) #we want the owner of the todo to be the user that created it

 


# class CreateTodoAPIView(CreateAPIView):


#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)#we want the user to be authenticated before creating a todo

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user) #we want the owner of the todo to be the user that created it

# class TodoListAPIView(ListAPIView):

#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)#we want the user to be authenticated before viewing the todos

#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user) #we want the owner of the todo to be the user that created it
