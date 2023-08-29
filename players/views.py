from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LoginForm, NewUserForm


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


@login_required(login_url='/login/')
def index(request: HttpRequest):
    user = request.user

    context = {
        'number_of_notifications': get_number_of_notifications_for_user(),
        'number_of_messages': get_number_of_messages_for_user(),
        'short_user_name': get_short_user_name(user),
        'long_user_name': get_long_user_name(user),
        'grade': get_grade(),
    }

    return render(request, 'index.html', context=context)


def login(request: HttpRequest):
    next_page = None
    errors = None

    if request.method == 'GET':
        next_page = request.GET.get('next')
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', '/players/'))
                else:
                    errors = 'Username is inactive!'
            else:
                errors = 'Username or password invalid!'
        else:
            errors = 'Fill both username and password!'
    else:
        form = LoginForm()

    return render(request, 'pages-login.html', {'form': form, 'next': next_page, 'errors': errors})


def logout(request: HttpRequest):
    django_logout(request)
    return HttpResponseRedirect('/players/')


def fetch_user(request: HttpRequest):
    return HttpResponse('')


def register(request):
    errors = {}
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect('index')
        errors = form.errors
    return render(request, 'register.html', context={'form': form, 'errors': errors})
