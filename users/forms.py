from pyexpat import model
from django import  forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import fields

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    username = forms.CharField()
    password = forms.CharField()
            

    # username = forms.CharField(
    #     label="Имя пользователя",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   "class":"form-control",
    #                                   "placeholder":"Введите имя пользователя",
    #                                   }
    # ))
    # password = forms.CharField(
    #     label="Пароль",
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       "class":"form-control",
    #                                       "placeholder":"Введите ваш пароль",
    #                                       }),
    #         )
    
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
             
            'first_name', 
            'last_name', 
            'email', 
            'username',
            'password1', 
            'password2'
            )
        
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        username = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()

