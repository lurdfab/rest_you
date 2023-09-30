from todolist.models import Todo
from rest_framework import serializers  



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ("id", "title", "description", "is_completed") #these are the fields we want to appear on the client side / converted from the model to json