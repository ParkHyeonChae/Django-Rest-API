from django.urls import include, path
from rest_framework import routers
from allauth.account.views import confirm_email

app_name = "accounts"

urlpatterns = [
    path('auth/', include("rest_auth.urls")),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/registration/account-confirm-email/<key>', confirm_email, name='account_confirm_email'),
]