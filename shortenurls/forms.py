from socket import fromshare
from django import forms
from .models import URL

class URLShortenForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['yourURL']
