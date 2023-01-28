from django.db import models

class TelegramUser(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,null=True,blank=True)
    user_id = models.CharField(max_length=10,unique=True)
    language = models.CharField(max_length=10,null=True,blank=True)


    def __str__(self):
        return self.first_name
