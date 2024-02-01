from django.contrib import admin
from .models import UserChoices, Messages
# Register your models here.
admin.site.register(UserChoices)
admin.site.register(Messages)