from django.shortcuts import render
from django.http import HttpResponse

# /app_one/

# available services

services = {
    'service_alfa': 'service_alfa',
    'service_beta': 'service_beta',
    'service_gamma': 'service_gamma'
}

# functions views

def index(request):
    return HttpResponse("Hello, world. You're at the app_one index.")

def service_view(request, service_name):
    return HttpResponse(f"Hello, world. You're at the {services[service_name]} section.")