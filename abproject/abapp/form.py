from abapp.models import emp1,emp2
from django import forms

class empform(forms.ModelForm):
    class Meta:
        model=emp1
        fields="__all__"

class loginform(forms.ModelForm):
    class Meta:
        model=emp2
        fields="__all__"