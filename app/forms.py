from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(label="",
        widget = forms.TextInput(attrs={
            'class': 'text_comment_form',
            'placeholder': 'Todo ...'
        })
    )
