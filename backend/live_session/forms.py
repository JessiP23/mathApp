from django import forms
from .models import SetSession

#form associated with a model
class SessionForm(forms.ModelForm):
    class Meta:
        #form associated with SetSession model
        model = SetSession
        #fields from the model
        fields = ['calendar', 'subject', 'time_hour', 'question']
        #individual fields customization
        widgets = {  
            #connect html attributes for widget
            'calendar': forms.DateInput(attrs={'type':'date'}),
            'time_hour': forms.TimeInput(attrs={'type':'time'}),
        }
    
    #options displayed in subject
    subjec_options = [
        ('', 'Select a subject'),
        ('Placement Test', 'Placement Test'),
        ('Basic Mathematics', 'Basic Mathematics'),
        ('Accelerated Algebra', 'Accelerated Algebra'),
        ('Precalculus', 'Precalculus'),
        ('CalculusI', 'CalculusI'),
    ]

    # Allow user to choose an option from the subject
    subject = forms.ChoiceField(choices=subjec_options, required=True, label='Subject')

