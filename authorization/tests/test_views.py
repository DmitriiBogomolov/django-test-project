from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthorizationPagesTests(TestCase):

    def test_auth_page(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_register_page(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)


class AuthorizationPostTests(TestCase):

    def setUp(self):
        User.objects.create_user('testuser', 'testuser@gmail.com',
                                 'testpassword123')
        self.user = User.objects.get(username='testuser')

    def test_login(self):
        resp = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'testpassword123'}
            )

        self.assertEqual(resp.status_code, 200)
        self.client.login(username='testuser', password='testpassword123')
        resp = self.client.get(reverse('message'))
        self.assertEqual(resp.context["user"], self.user)

    def test_register(self):
        resp = self.client.post(
            reverse('register'),
            {'username': 'testuser1', 'password1': 'testpassword123',
             'email': 'testuser1@gmail.com', 'password2': 'testpassword123'}
            )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser1').exists())
