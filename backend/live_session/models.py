from django.db import models
from django.contrib.auth.models import User

class SetSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar = models.DateField()
    subject = models.CharField(max_length=60)
    time_hour = models.TimeField()
    question = models.TextField(default='')

    #string representation
    def __str__(self): 
        return f"User: {self.user.username}, date: {self.calendar}, and subject: {self.subject}"
