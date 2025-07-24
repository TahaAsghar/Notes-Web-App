from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter title here...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Write your note...'
            }),
        }
