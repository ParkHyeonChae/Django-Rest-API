from django.urls import include, path, re_path
from rest_framework import routers
from allauth.account.views import confirm_email

app_name = "accounts"


# from django.contrib.auth import get_user_model
# from django.shortcuts import redirect
# from django.http import Http404
# from django.urls import reverse

# class CustomConfirmEmailView(ConfirmEmailView):
#     def get(self, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             self.object = None
#         user = get_user_model().objects.get(email=self.object.email_address.email)
#         redirect_url = reverse('user', args=(user.id,))
#         return redirect(redirect_url)

urlpatterns = [
    path('auth/', include("rest_auth.urls")),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    # path('auth/registration/account-confirm-email/<slug:key>', confirm_email, name='account_confirm_email'),
    re_path('auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$/', confirm_email, name='account_confirm_email'),
]