"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from messager.views import Messager
from authorization.views import LoginPage, Register, Logout, Login

urlpatterns = [
    url(r'^login/authorize/$', Login.as_view(), name='login'),
    url(r'^login/$', LoginPage.as_view(), name='loginPage'),
    url(r'^register/$', Register.as_view(), name='registerPage'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^sendMessage/$', Messager.as_view(), name='sendMessage'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Messager.as_view(), name='message'),
]
