from django.db import models
from django.contrib.auth.models import User

class SetSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar = models.DateField()
    subject = models.CharField(max_length=60)
    time_hour = models.TimeField()
    question = models.TextField(default='Enter any questions')

    def __str__(self):
        return f"Session for {self.user.username} on {self.calendar} - Subject: {self.subject}"
