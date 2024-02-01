from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserChoices(models.Model):
    
    username = models.CharField(max_length = 100, unique = True)
    userphoto = models.ImageField(upload_to="images/", default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_name', null = True, blank=True)
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user1_related')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user2_related')
    user3 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user3_related')
    enrollment_number = models.BigIntegerField(unique= True)
    bio = models.CharField(max_length = 255)
    CHOICES1 = [
        ('Dating', 'Dating'),
        ('Single', 'Single'),
        ('Long Distance', 'Long Distance'),
    ]
    status = models.CharField(max_length=100,choices = CHOICES1)
    CHOICES2 = [
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Electronics', 'Electronics'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Economics', 'Economics'),
        ('Computer Science', 'Computer Science'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Eph', 'Eph'),
        ('Mathematics and Computing','Mathematics and Computing'),
        ('GPT','GPT'),
        ('GT', 'GT'),
        ('Metallurgy', 'Metallurgy'),
        ('Biotech','Biotech'),
        ('Chemical Science','Chemical Science'),
        ('DSAI','DSAI'),
        ('PnI','PnI'),
        ('Architecture','Architecture'),
    
    ]
    CHOICES3 = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather not say', 'Rather not say'),
    ]
    gender = models.CharField(max_length = 20, choices = CHOICES3, default = "Rather not say")
    branch = models.CharField(max_length = 100, choices = CHOICES2)
    
    def __str__(self):
        return self.username
    def upload(self):   
        
        self.save()


class Messages(models.Model):


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='username1')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='username2')
    date = models.DateTimeField(blank = True, null = True)
    class Meta:
        # Ensure that the combination of field1 and field2 is unique
        unique_together = ['user', 'from_user']

    def upload(self):
        self.date = timezone.now()
        self.save()

# class Choices(models.Model):
    
#     username = models.CharField(max_length = 100, unique = True)
#     userphoto = models.URLField(null = True, blank = True)
#     from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from')
#     to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to')
#     user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user1_related', blank=True, null = True)
#     user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user2_related', blank = True, null = True)
#     user3 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user3_related', blank = True, null = True)
#     class Meta:
#         # Ensure that the combination of field1 and field2 is unique
#         unique_together = ['user', 'from_user']

   