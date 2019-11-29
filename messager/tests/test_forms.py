from django.test import TestCase
from messager.forms import MessageForm


class MessageFormLabelsTest(TestCase):
    def test_email_label(self):
        form = MessageForm()
        self.assertTrue(form.fields['email'].label is None or
                        form.fields['email'].label == 'email')

    def test_message_label(self):
        form = MessageForm()
        self.assertTrue(form.fields['message'].label is None or
                        form.fields['message'].label == 'message')
