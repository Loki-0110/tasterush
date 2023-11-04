from django import forms

from user.models import User


class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        field = "__all__"
        exclude = ["id"]