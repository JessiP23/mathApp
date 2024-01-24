from django import forms
from .models import SetSession
from django.utils.safestring import mark_safe

class SessionForm(forms.ModelForm):
    class Meta:
        model = SetSession
        fields = ['calendar', 'subject', 'time_hour', 'question']
        widgets = {
            'calendar': forms.DateInput(attrs={'type':'date'}),
            'time_hour': forms.TimeInput(attrs={'type':'time'}),
            'subject': forms.Select(attrs={'onchange': 'price()'}),
        }

    SUBJECT_CHOICES = [
        ('', 'Select a subject'),
        ('Placement Test', 'Placement Test'),
        ('Basic Mathematics', 'Basic Mathematics'),
        ('Accelerated Algebra', 'Accelerated Algebra'),
        ('Precalculus', 'Precalculus'),
        ('CalculusI', 'CalculusI'),
    ]

    # Add choices to the subject field
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, required=True, label='Subject')

