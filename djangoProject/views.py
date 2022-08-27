from django.http import HttpResponse
import logging

from django.shortcuts import render
from django.views.generic import TemplateView

_logger = logging.getLogger(__name__)


class Maintenance(TemplateView):
    template_name = "maintenance.html"


class NotFound(TemplateView):
    template_name = "404.html"


class HomePage(TemplateView):
    template_name = "homepage.html"




