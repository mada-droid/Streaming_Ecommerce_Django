"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import handler404
from django.contrib import admin
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import include, path
from django.contrib.auth import views as auth_views

from djangoProject.views import Maintenance, HomePage, NotFound, UserDashBoard, UserCreateView

urlpatterns = [
    path("", HomePage.as_view(), name="home-page"),
    path("maintenance/", Maintenance.as_view(), name="maintenance"),
    path('admin/', admin.site.urls, name="admin-dash"),
    path('404/', NotFound.as_view(), name="404-Not-Found"),
    path("blog/", include("blog.urls")),
    path("user_dash_board/", UserDashBoard.as_view(), name="user-dash-board"),
    path("user_registeration/", UserCreateView.as_view(), name="register"),
    path("user_login/", auth_views.LoginView.as_view(), name="login"),
    path("user_logout/", auth_views.LogoutView.as_view(), name="logout"),
]

urlpatterns += staticfiles_urlpatterns()




