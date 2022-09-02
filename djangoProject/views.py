from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

_logger = logging.getLogger(__name__)


class Maintenance(TemplateView):
    template_name = "maintenance.html"


class NotFound(TemplateView):
    template_name = "404.html"


class HomePage(TemplateView):
    template_name = "home_page_v3.html"


class UserDashBoard(TemplateView):
    template_name = "user/dash_board.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/user_create.html'
    success_url = reverse_lazy('home-page')
