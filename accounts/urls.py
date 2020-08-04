from django.urls import include, path
from rest_framework import routers


app_name = "accounts"

urlpatterns = [
    path('rest-auth/', include("rest_auth.urls")),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]