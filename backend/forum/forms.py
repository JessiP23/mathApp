from django import forms
from .models import PostQuestion, Comment

class FormatQuestion(forms.ModelForm):
    class Meta:
        model = PostQuestion
        fields = ['title','description']

class CommentFormat(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']