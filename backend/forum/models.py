from django.db import models
from django.contrib.auth.models import User

class PostQuestion(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timepost = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_related = models.ForeignKey(PostQuestion, related_name='comments', on_delete=models.CASCADE)