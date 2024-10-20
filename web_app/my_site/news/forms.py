from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from datetime import datetime


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва допису',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': f'Дата публікації, напр: {datetime.now().strftime("%Y-%m-%d %H:%M:%S ")}'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст допису',
            }),
        }