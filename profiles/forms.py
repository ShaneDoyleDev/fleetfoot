from django import forms
from .models import Profile, Review, Rating


class ProfileForm(forms.ModelForm):
    """
    A form for creating or updating user profiles.
    """
    class Meta:
        model = Profile
        exclude = ('user',)


class ReviewForm(forms.ModelForm):
    """
    A form for creating or updating a review.
    """
    class Meta:
        model = Review
        fields = ['title', 'content']


class RatingForm(forms.ModelForm):
    """
    A form for creating or updating a rating.
    """
    class Meta:
        model = Rating
        fields = ['score']
