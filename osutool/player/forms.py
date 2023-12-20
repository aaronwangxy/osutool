from django import forms

class PlayerName(forms.Form):
    playername = forms.CharField(label="Username", max_length=100)