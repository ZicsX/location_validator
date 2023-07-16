from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(label='Store Locator URL', max_length=200)
