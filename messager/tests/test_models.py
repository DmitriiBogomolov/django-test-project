from django.test import TestCase
from messager.models import Message
from datetime import datetime
from django.contrib.auth.models import User


class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('testuser', 'testuser@gmail.com',
                                 'qwerty12345')
        Message.objects.create(email="testing@email.com",
                               message="testingmessage",
                               date=datetime.now(),
                               sent=True,
                               user=User.objects.get(id=1))

    def test_email_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_message_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'message')

    def test_date_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_sent_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('sent').verbose_name
        self.assertEquals(field_label, 'sent')

    def test_email_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('email').max_length
        self.assertEquals(max_length, 35)

    def test_message_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('message').max_length
        self.assertEquals(max_length, 255)
