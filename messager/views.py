from django.shortcuts import render
from django.views.generic import View
from .forms import MessageForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import json
import requests
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class Messager(View):
    def get(self, request):
        username = request.user.username
        email = request.user.email
        messageForm = MessageForm({"email": email})
        return render(request, "messager.html",
                      {"form": messageForm, "username": username})

    def post(self, request):
        messageForm = MessageForm(request.POST)
        if messageForm.is_valid():

            username = request.user.username
            email = messageForm.cleaned_data['email']
            message = messageForm.cleaned_data['message']

            foundData = self.getInfo(email)
            formatData = self.formatData(foundData, message, email)
            sent = self.sendEmail(username, formatData)

            messageForm.save(request.user, sent)

            return HttpResponse("ok", content_type='text/html')
        else:
            return HttpResponse(json.dumps(messageForm.errors),
                                content_type='application/json')

    def getInfo(self, email):
        IMPORT_URL = 'http://jsonplaceholder.typicode.com/users'
        headers = {'Content-Type': 'application/json'}
        data = requests.get(url=IMPORT_URL, headers=headers).json()

        foundData = []
        for user in data:
            if user["email"] == email:
                foundData.append(user)

        return foundData

    def formatData(self, data, message, email):
        data = json.dumps(data, sort_keys=True, indent=4)

        excludes = ['[', ']', '"', ',', '{', '}']
        for symbol in excludes:
            data = data.replace(symbol, "")
        if data != "":
            data = "Here is data found in JSON service:\n" + data

        formatedData = f"{message}\n User email: {email}\n\n\n{data}"

        return formatedData

    def sendEmail(self, username, formatData):
        sent = send_mail('This message from ' + username,
                         formatData, settings.EMAIL_HOST_USER,
                         [settings.ADMIN_EMAIL], fail_silently=False)
        return sent
