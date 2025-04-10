from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','body']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)
        
        # Clear help text
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
            