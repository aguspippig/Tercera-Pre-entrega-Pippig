from django import forms 

class CargaProcesador(forms.Form):
    marca=forms.CharField(max_length=128)
    modelo=forms.CharField(max_length=128)
    stock=forms.IntegerField(required=True)
   
    
class CargaPlacaMadre(forms.Form):
    marca=forms.CharField(max_length=128)
    modelo=forms.CharField(max_length=128)
    stock=forms.IntegerField(required=True)
   


class CargaRam(forms.Form):
    marca=forms.CharField(max_length=128)
    modelo=forms.CharField(max_length=128)
    stock=forms.IntegerField(required=True)
       