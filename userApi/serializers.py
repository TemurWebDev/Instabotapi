from rest_framework import serializers
from .models import TelegramUser,Admin,Reklama,Channel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class ReklamaSerializzers(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = '__all__'



class ChannelSerializzers(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'



