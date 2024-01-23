from django import forms
from .models import PostQuestion

class FormatQuestion(forms.ModelForm):
    class Meta:
        model = PostQuestion
        fields = ['title','description']