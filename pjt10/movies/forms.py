from .models import Reviews
from django import forms

class ReviewsModelForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('content', 'score',)
