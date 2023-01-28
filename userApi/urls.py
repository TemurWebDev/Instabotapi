from django.urls import path
from .views import UserApiView,UserUpdateApiView

urlpatterns = [
    path('telegramuser/',UserApiView.as_view()),
    path('userupdate/<int:pk>/',UserUpdateApiView.as_view()),
]
