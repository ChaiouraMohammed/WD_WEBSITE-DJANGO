# forms.py

from django import forms
from .models import CSVFile
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



class CSVFileForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ['file']
