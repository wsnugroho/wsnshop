from django.forms import ModelForm
from django.utils.html import strip_tags

from main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]

    def clean_name(self):
        mood = self.cleaned_data["name"]
        return strip_tags(mood)

    def clean_description(self):
        feelings = self.cleaned_data["description"]
        return strip_tags(feelings)
