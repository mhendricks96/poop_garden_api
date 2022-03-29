from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class PoopProfile(models.Model):
  poopInfo = models.IntegerField()
  nickname = models.CharField(max_length=64)
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nickname

# class FriendList(models.Model):
#   user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#   # friends = Friend.objects.friends(get_user_model())

#   def __str__(self):
#     return self.user