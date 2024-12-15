from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class TextAnalysisForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Enter your text here..."}),
        label="Copywriting Sample"
    )

