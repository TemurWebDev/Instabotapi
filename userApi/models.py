from django.db import models

class TelegramUser(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,null=True,blank=True)
    user_id = models.CharField(max_length=10,unique=True)
    language = models.CharField(max_length=10,null=True,blank=True)


    def __str__(self):
        return self.first_name


class Admin(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name


class Reklama(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images',null=True,blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name