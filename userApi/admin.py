from django.contrib import admin
from .models import TelegramUser,Admin,Reklama,Channel

# Register your models here.
admin.site.register(TelegramUser)
admin.site.register(Admin)
admin.site.register(Reklama)
admin.site.register(Channel)

