from django import forms
from .models import Book, Description


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
        ]

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = [
            'text',
        ]