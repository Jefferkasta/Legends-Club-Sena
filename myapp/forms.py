from django.forms import ModelForm
from .models import Article
from loginUser.models import User
from django import forms

class formArtic(ModelForm):
    class Meta:
        model = Article
        fields = ['nameArticle', 'categoryArticle', 'descriptionArticle', 'priceArticle','activeArticle'] 

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['identificationUser','emailUser','firstnameUser', 'lastnameUser','ageUser', 'phoneUser','appointmentUser','imageUser','activeUser','adminUser']
       
