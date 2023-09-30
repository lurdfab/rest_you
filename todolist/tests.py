from rest_framework.test import APITestCase
from django.urls import reverse



class TestListCreateTodo(APITestCase):


    def authenticate(self):
        self.client.post(reverse("register"), {"username": "username"}, {"email": "email@gmail.com", "password": "password"})
        response = self.client.post(reverse("login"), {"username": "username"}, {"email": "email@gmail.com", "password": "password"})
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {response.data['token']}")

    def test_should_not_create_todo_with_no_auth(self):
        sample_todo = {"title": "test todo", "description": "test description"}
        response = self.client.post(reverse("list-create"), sample_todo)
        self.assertEqual(response.status_code, 401)

    def test_should_create_todo(self):
        self.authenticate()
        sample_todo = {"title": "test todo", "description": "test description"}
        response = self.client.post(reverse("list-create"), sample_todo)
        self.assertEqual(response.status_code, 201)