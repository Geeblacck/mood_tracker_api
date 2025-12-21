from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AuthTests(APITestCase):

    def test_user_signup(self):
        url = reverse('signup')  # must match your URL name
        data = {
            "username": "testuser",
            "password": "strongpassword123"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())


    def test_user_login_returns_token(self):
        User.objects.create_user(
            username="testuser",
            password="strongpassword123"
        )

        url = reverse('login')
        data = {
            "username": "testuser",
            "password": "strongpassword123"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
