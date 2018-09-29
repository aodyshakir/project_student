from django import forms

class UserRegistrar(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_bith = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))


class DegreeRegistrar(forms.Form):
    student_drgee = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))