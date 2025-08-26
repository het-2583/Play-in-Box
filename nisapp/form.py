from .models import UserModel  # Import your custom UserModel here
from django import forms
from .models import Team
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm

# Your custom user creation form with UserModel
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )




class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'city_town', 'captain_phone', 'captain_name']






class SignUpForm(UserCreationForm):
    
    USER_TYPE_CHOICES = (
    ('Doctor', 'doctor'),
    ('Patient', 'patient') 
    )

    type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(

        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    userProfile = forms.ImageField(
        required=False,  # Set to True if you want to make it required
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control-file"
            }
        )
    )
    # Add a field for the profile picture
    

    class Meta:
        model = UserModel
        fields = ('username', 'userProfile', 'first_name', 'last_name', 'email')



