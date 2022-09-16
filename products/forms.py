from django import forms

class Form_products (forms.Form):
    name=forms.CharField(max_length=40)
    price=forms.FloatField()
    stock=forms.IntegerField()
    image=forms.ImageField(required=False)
    

