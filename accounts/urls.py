from accounts.views import AccountView, LoginJWTView
from django.urls import path

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("login/", LoginJWTView.as_view()),
]
