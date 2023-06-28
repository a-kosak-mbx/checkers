from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def get_number_of_notifications_for_user() -> int:
    return 10


def get_number_of_messages_for_user() -> int:
    return 4


def get_short_user_name(user) -> str:
    # print(dir(user))
    return f"{user.first_name[0] + '. ' if user.first_name else ''}{user.last_name}"


def get_long_user_name(user) -> str:
    return f'{user.first_name} {user.last_name}'


def get_grade() -> str:
    return 'Junior'


def index(request: HttpRequest):
    user = request.user
    if user.is_authenticated:
        context = {
            'number_of_notifications': get_number_of_notifications_for_user(),
            'number_of_messages': get_number_of_messages_for_user(),
            'short_user_name': get_short_user_name(user),
            'long_user_name': get_long_user_name(user),
            'grade': get_grade(),
        }

    return render(request, 'index.html', context=context)


def fetch_user(request: HttpRequest):
    return HttpResponse('')
