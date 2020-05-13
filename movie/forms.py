from django import forms

class NameForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)