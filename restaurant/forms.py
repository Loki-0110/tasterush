from django import forms

from restaurant.models import Restaurant


class RestaurantRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Restaurant
        field = "__all__"
        exclude = ["id"]