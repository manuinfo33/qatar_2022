from django import forms

class Form_news (forms.Form):
    title=forms.CharField(max_length=40)
    description=forms.CharField(max_length=1000)
    author=forms.CharField(max_length=40)
    
