from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
# forms.Form 无sql操作 forms.ModelForm 有数据库操作


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User  # 声明数据模型,也就是数据会写入哪个库表中的哪些字段
        fields = ("username", "email") # 声明需要赋值的字段，也可以使用exclude排除属性

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password don't match.")
        return cd['password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")
