from rest_framework.test import APITestCase
from authentication.models import User


class TestModels(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user("jonathan", "agbornah@gmail.com", "password123")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "agbornah@gmail.com")

    def test_create_super_user(self):
        user = User.objects.create_superuser("jonathan", "agbornah@gmail.com", "password123")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "agbornah@gmail.com")


    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email="agbornah@gmail.com", password="password123")

    
    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="jonathan", email="", password="password123")

    def test_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True." ):
            User.objects.create_superuser(username="jonathan", email="agbornah@gmail.com", password="password123", is_staff=False) 

    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(username="jonathan", email="agbornah@gmail.com", password="password123", is_superuser=False) 