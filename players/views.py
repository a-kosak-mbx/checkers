from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'index.html')


def fetch_user(request: HttpRequest):
    return HttpResponse('')
