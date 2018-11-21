from django import forms
from blog.models import BLOG

class Form (forms.ModelForm):
    class Meta:
        model = BLOG
        fields = ('title', 'content')
