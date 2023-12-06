from django.forms import ModelForm
from .models import Article
from loginUser.models import User
from django import forms
from django.contrib.auth.models import User

class formArtic(ModelForm):
    class Meta:
        model = Article
        fields = ['nameArticle', 'categoryArticle', 'descriptionArticle', 'priceArticle','activeArticle'] 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstnameUser', 'lastnameUser', 'emailUser', 'ageUser', 'phoneUser']
        # Agrega otros campos según tus necesidades
