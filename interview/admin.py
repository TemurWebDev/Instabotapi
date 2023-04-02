from django.contrib import admin
from .models import Category,InterviewQuestions,InterviewAnswer

# Register your models here.
admin.site.register(Category)
admin.site.register(InterviewQuestions)
admin.site.register(InterviewAnswer)

