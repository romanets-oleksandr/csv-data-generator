# -*- encoding: utf-8 -*-
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import login_view


urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
