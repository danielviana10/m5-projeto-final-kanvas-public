from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import Account
from accounts.serializers import AccountSerializer


# Create your views here.
class AccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginJWTView(TokenObtainPairView):
    serializer_class = AccountSerializer.CustomJWTSerializer
