from authentication.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True) #we used write only because we don't want it returned back to the server


    class Meta:
        model = User
        fields = ("username", "email", "password") #these are the fields we want to appear on the client side / converted from the model to json


    #this method is used to create the user but it this isn't the default but overidden by the create method below
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) #this is the method that creates the user
    

class LoginSerializer(serializers.ModelSerializer):


    password = serializers.CharField(max_length=128, min_length=8, write_only=True) #we used write only because we don't want it returned back to the server


    class Meta:
        model = User
        fields = ("username","email", "password", "token") #these are the fields we want to appear on the client side / converted from the model to json
        read_only_fields = ["token"] #we don't want the token to be written or saved to the database/server but handled by the application
