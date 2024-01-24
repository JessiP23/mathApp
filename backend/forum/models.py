from django.db import models
from django.contrib.auth.models import User

def file_url(instance, filename):
    #store images uploaded by user in the comment section
    url = f'question_images/{instance.user.username}/{filename}'
    print(f"File URL: {url}")
    return url

class PostQuestion(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #upload files to the directory above
    file = models.ImageField(upload_to=file_url, null=True, blank=True)
    timepost = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #If a post is deleted, will delete the comment
    question_related = models.ForeignKey(PostQuestion, related_name='comments', on_delete=models.CASCADE)