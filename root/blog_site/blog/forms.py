from dataclasses import field
from django.forms import ModelForm
from .models import blog

class blog_form(ModelForm):
    class Meta:
        model=blog
        fields=['author', 'Date','Description']