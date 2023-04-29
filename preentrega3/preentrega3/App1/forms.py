from django import forms

class GuitarrasFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    color= forms.CharField(max_length=30)



