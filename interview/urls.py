from django.urls import path
from .views import CategoryView,InterviewqView,InterviewAView,QuestionView,AnswerView


urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('questions/',InterviewqView.as_view()),
    path('question/<str:category_name>/',QuestionView.as_view()),
    path('answer/',InterviewAView.as_view()),
    path('answer/<str:slug>/',AnswerView.as_view()),
]