from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse('Just empty text page')


def fetch_user(request: HttpRequest):
    return HttpResponse('Just empty text page')
