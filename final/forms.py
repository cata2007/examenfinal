from django import forms

class UsersForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.EmailField(required=False)
    number_of_login =forms.IntegerField()