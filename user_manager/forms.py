from django import forms

class JoinForm(forms.Form):
    """회원가입 폼을 정의한다."""

    id = forms.CharField(label="ID", min_length=4, max_length=12,
        required=True, help_text='4자이상 12자 미만으로 입력하세요')
    password = forms.CharField(label="PASSWORD", min_length=6, max_length=12,
        widget = forms.PasswordInput, required=True,
        help_text='6자 이상 12자 미만으로 입력하세요')
    password_check = forms.CharField(label="PASSWORD(again)", min_length=6,
        max_length=12, widget = forms.PasswordInput, required=True,
        help_text='위의 패스워드와 동일하게 입력되어야 합니다.')

    def clean(self):
        cleaned_data = super(JoinForm, self).clean()
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')

        if password != password_check:
            raise forms.ValidationError(
                "패스워드가 서로 일치하지 않습니다."
            )
