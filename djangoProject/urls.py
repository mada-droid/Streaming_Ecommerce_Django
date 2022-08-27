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

from django.urls import include, path

from djangoProject.views import Maintenance, HomePage, NotFound

urlpatterns = [
    path("", HomePage.as_view(), name="home-page"),
    path("maintenance/", Maintenance.as_view(), name="maintenance"),
    path('admin/', admin.site.urls),
    path('404/', NotFound.as_view(), name="404-Not-Found"),
    path("blog/", include("blog.urls")),
]


# handler404 = "blog.views.handle_not_found"



