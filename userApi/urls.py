from django.urls import path
from .views import UserApiView,UserUpdateApiView,UserView,AdminUpdateView,AdminView,ReklamaView,ChannelUpdateView,ChannelView

urlpatterns = [
    path('telegramuser/',UserApiView.as_view()),
    path('user/<str:user_id>/',UserView.as_view()),
    path('userupdate/<int:pk>/',UserUpdateApiView.as_view()),
    path('admin/',AdminView.as_view()),
    path('admin/delete/<str:user_id>/',AdminUpdateView.as_view()),
    path('reklama/',ReklamaView.as_view()),
    path('channel/',ChannelView.as_view()),
    path('channel/delete/<str:channel_id>/',ChannelUpdateView.as_view()),

]
