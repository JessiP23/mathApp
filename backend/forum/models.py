from django.db import models
from django.contrib.auth.models import User

class PostQuestion(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timepost = models.DateTimeField(auto_now_add=True)

