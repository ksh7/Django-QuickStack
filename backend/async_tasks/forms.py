from django import forms

class WebsiteCarbonFootprintdForm(forms.Form):

    url = forms.CharField(label='Website URL', max_length=100, min_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))
