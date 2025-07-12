#forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 rounded border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-2 rounded border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full px-4 py-2 rounded border focus:outline-none focus:ring-2 focus:ring-blue-500',
        'placeholder': 'Your Message',
        'rows': 4
    }))