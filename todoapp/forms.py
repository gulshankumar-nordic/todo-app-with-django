from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=75,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )