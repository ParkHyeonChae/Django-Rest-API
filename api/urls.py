"""api/urls.py"""

from django.urls import path
from . import views


urlpatterns = [
    path("auth/register/", views.RegistrationAPI.as_view()),
    path("auth/login/", views.LoginAPI.as_view()),
    path("auth/user/", views.UserAPI.as_view()),
]