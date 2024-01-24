from django import forms
from .models import PostQuestion, Comment

#inherited class from models that is used in templates
class FormatQuestion(forms.ModelForm):
    class Meta:
        model = PostQuestion
        fields = ['title', 'file' ,'description']

class CommentFormat(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']