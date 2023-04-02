from rest_framework import serializers
from .models import Category,InterviewQuestions,InterviewAnswer

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class InterviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestions
        fields = '__all__'


class InterviewAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = InterviewAnswer
        fields = '__all__'


