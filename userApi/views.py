from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import TelegramUser
from .serializers import UserSerializer



class UserApiView(ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer
