from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import CategorySerializers,InterviewSerializers,InterviewAnswerSerializers
from .models import Category,InterviewQuestions,InterviewAnswer
from rest_framework.response import Response


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class InterviewqView(ListCreateAPIView):
    queryset = InterviewQuestions.objects.all()
    serializer_class = InterviewSerializers


class QuestionView(APIView):
    def get(self,request,category_name):
        questions = InterviewQuestions.objects.filter(category__name=category_name)
        serializer = InterviewSerializers(questions,many=True)
        return Response(serializer.data)



class InterviewAView(ListCreateAPIView):
    queryset = InterviewAnswer.objects.all()
    serializer_class = InterviewAnswerSerializers





class AnswerView(APIView):
    def get(self,request,slug):
        answer = InterviewAnswer.objects.filter(question__question=slug)
        serializer = InterviewAnswerSerializers(answer,many=True)
        return Response(serializer.data)
