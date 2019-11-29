from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from .forms import LoginForm, RegisterForm
import json

# Create your views here.
class LoginPage(View):
    def get(self, request):
        loginForm = LoginForm()
        return render(request, "login.html", {"form": loginForm})


class Login(View):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        data = {'username': username, 'password': password}
        loginForm = LoginForm(data)

        if loginForm.is_valid():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponse("ok", content_type='text/html')
            else:
                return HttpResponse("login_error", content_type='text/html')
        else:
            return HttpResponse(json.dumps(loginForm.errors),
                                content_type='application/json')


class Register(View):
    def get(self, request):
        if not request.user.is_authenticated:
            registerForm = RegisterForm()
            return render(request, "register.html", {'form': registerForm})
        else:
            return redirect('message')

    def post(self, request):
        if not request.user.is_authenticated:

            registerForm = RegisterForm(request.POST)
            if registerForm.is_valid():
                user = registerForm.save()
                user = auth.authenticate(username=request.POST["username"],
                                         password=request.POST["password"])
                if user is not None:
                    auth.login(request, user)
                return HttpResponse("ok", content_type='text/html')
            else:
                return HttpResponse(json.dumps(registerForm.errors),
                                    content_type='application/json')

        else:
            return HttpResponseForbidden()


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('loginPage')
