from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import CollaborateRequest
        
class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = [
                    'name',
                    'email',
                    'message',
        ]
        widgets = {
            'message': SummernoteWidget(),
        }