# forms.py
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject')
    recipient = forms.EmailField(label='Recipient Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
