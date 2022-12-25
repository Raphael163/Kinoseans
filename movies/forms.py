from django import forms


from .models import Reviews


class ReviewForm(forms.ModelForm):
    """ FORMA отзыва"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")

