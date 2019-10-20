from django import forms
from .models import Movie, Review

class MovieModelForm(forms.ModelForm):
    class Meta():
        model = Movie
        fields = '__all__'

class ReviewModelForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = ('content', 'score', )