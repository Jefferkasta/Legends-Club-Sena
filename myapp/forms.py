from django.forms import ModelForm
from .models import Article

class formArtic(ModelForm):
    class Meta:
        model = Article
        fields = ['nameArticle', 'categoryArticle', 'descriptionArticle', 'priceArticle','activeArticle'] 