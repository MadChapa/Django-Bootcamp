from django import forms
from second_app.models import *

class NewUserForm(forms.ModelForm):
    class Meta():
        model=User
        fields='__all__'
