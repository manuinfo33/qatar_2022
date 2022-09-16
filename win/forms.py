from django import forms

class Form_participants (forms.Form):
    name=forms.CharField(max_length=40)
    document=forms.IntegerField()
    age=forms.IntegerField()
    country=forms.CharField(max_length=50)
    description=forms.CharField(max_length=400)