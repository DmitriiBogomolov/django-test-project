from django.test import TestCase
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class AuthorizationPagesTests(TestCase):

    def test_auth_page(self):
        resp = self.client.get(reverse('loginPage'))
        self.assertEqual(resp.status_code, 200)

    def test_register_page(self):
        resp = self.client.get(reverse('registerPage'))
        self.assertEqual(resp.status_code, 200)


class AuthorizationPostTests(TestCase):

    def setUp(self):
        User.objects.create_user('testuser', 'testuser@gmail.com',
                                 'qwerty12345')
        self.user = User.objects.get(username='testuser')

    def test_login(self):
        resp = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'qwerty12345'}
            )

        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('loginPage'))
        self.assertEqual(resp.context["user"], self.user)

    def test_register(self):
        resp = self.client.post(
            reverse('registerPage'),
            {'username': 'testuser1', 'password': 'qwerty12345',
             'email': 'testuser1@gmail.com', 'confirm': 'qwerty12345'}
            )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser1').exists())
