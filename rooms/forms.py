from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(
        required=False, help_text="What is your highest amount you are willing to pay?"
    )
    guests = forms.IntegerField(
        required=False, help_text="How many people will be staying?"
    )
    bedrooms = forms.IntegerField(
        required=False, help_text="No. of bedrooms in the whole place"
    )
    beds = forms.IntegerField(
        required=False, help_text="No. of beds in the whole place"
    )
    baths = forms.IntegerField(
        required=False, help_text="No. of baths in the whole place"
    )
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
