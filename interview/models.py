from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class InterviewQuestions(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    question = models.TextField()


    def __str__(self):
        return self.question


class InterviewAnswer(models.Model):
    question = models.ForeignKey(InterviewQuestions,on_delete=models.CASCADE)
    answer = models.TextField()


    def __str__(self):
        return self.answer

