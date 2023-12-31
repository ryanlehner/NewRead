"""
URL configuration for newRead_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views

# shouldn't be necessary as the program should be 1 page
urlpatterns = [
    # admin page gives an admin option for the url
    path('admin/', admin.site.urls),
    # go to different page
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('about', views.about, name="about"),
    path('contact', views.conact, name="contact"),
    path('accounts/profile', views.ProfileView.as_view(), name="profile"),

    # Django Auth (login page)
    path('/accounts/login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('/accounts/logout', auth_views.LogoutView.as_view(), name="logout")
]
