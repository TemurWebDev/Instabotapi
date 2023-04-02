from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import TelegramUser,Admin,Reklama,Channel
from .serializers import UserSerializer,AdminSerializers,ReklamaSerializzers,ChannelSerializzers
from rest_framework.views import APIView
from rest_framework.response import Response



class UserApiView(ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer



class UserView(APIView):
    def get(self, request, user_id):
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id,format=None):
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdminView(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializers


class AdminUpdateView(APIView):
    def delete(self, request, user_id, format=None):
        admin = Admin.objects.get(user_id=user_id)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReklamaView(ListCreateAPIView):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializzers



class ChannelView(ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializzers


class ChannelUpdateView(APIView):
    def delete(self, request, channel_id, format=None):
        channel = Channel.objects.get(channel_id=channel_id)
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

