from django import forms

class LoginForm(forms.Form):
    """Login 폼을 정의해준다"""

    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12, widget = forms.PasswordInput)
