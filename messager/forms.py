from django import forms
from .models import Message
from datetime import datetime


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class MessageForm(PlaceholderForm):
    email = forms.EmailField(help_text='Email', min_length=5, max_length=35)
    message = forms.CharField(widget=forms.Textarea, min_length=10,
                              max_length=255, help_text='Your message')

    def save(self, user, sent):
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        date = datetime.now()
        sent = sent
        user = user
        newMessage = Message.objects.create(email=email, message=message,
                                            date=date, sent=sent, user=user)
        return newMessage
