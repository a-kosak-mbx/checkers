from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register"),
    path('fetch_user', views.fetch_user, name='fetch_user'),
]
