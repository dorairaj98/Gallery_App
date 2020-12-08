from django import forms
from .models import gallery_details

class galleryForm(forms.ModelForm):
    class Meta:
        model= gallery_details
        fields= ["gallery_category", "img"]