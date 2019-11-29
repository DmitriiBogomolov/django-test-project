from django.test import TestCase
import requests
from django.urls import reverse
from messager.views import Messager
from django.contrib.auth.models import User


class MessagerPagesTest(TestCase):

    def setUp(self):
        User.objects.create_user('testuser',
                                 'testuser@gmail.com',
                                 'qwerty12345')

    def test_messager_page(self):
        resp = self.client.get(reverse('message'))
        self.assertEqual(resp.status_code, 302)

        self.client.login(username='testuser', password='qwerty12345')
        resp = self.client.get(reverse('message'))
        self.assertEqual(resp.status_code, 200)


class MessagerPostTest(TestCase):

    def setUp(self):
        User.objects.create_user('testuser', 'testuser@gmail.com',
                                 'qwerty12345')

    def test_sendMessage(self):
        resp = self.client.post(
            reverse('sendMessage'),
            {"email": "testuser@gmail.com",
             "message": "testMessage"}
            )
        self.assertEqual(resp.status_code, 403)

        self.client.login(username='testuser', password='qwerty12345')
        resp = self.client.post(
            reverse('sendMessage'),
            {"email": "testuser@gmail.com",
             "message": "testMessage"}
            )
        self.assertEqual(resp.status_code, 200)


class MessagerFunctionsTest(TestCase):

    def test_getInfo(self):
        IMPORT_URL = 'http://jsonplaceholder.typicode.com/users'
        headers = {'Content-Type': 'application/json'}
        data = requests.get(url=IMPORT_URL, headers=headers).json()
        self.assertEqual(Messager.getInfo(self, "Sincere@april.biz")[0], data[0])

    def test_sendEmail(self):
        username = "testUserName"
        data = "testData"
        self.assertTrue(Messager.sendEmail(self, username, data))

    def test_formatData(self):
        testString = '[{ first:first, second:second }]'
        message = "message"
        email = "email"
        expectData = 'Here is data found in JSON service:\n first:first second:second '
        expectString = f"{message}\n User email: {email}\n\n\n{expectData}"
        self.assertEqual(Messager.formatData(self, testString, message, email), expectString)
