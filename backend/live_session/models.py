from django.db import models
from django.contrib.auth.models import User


class SetSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar = models.DateField()
    subject = models.TextField()
    time_hour = models.TimeField()
    question = models.TextField(default='Enter any questions')

   