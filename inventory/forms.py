from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'mass', 'unit',
                  'quantity',  'location', 'set_products', 'note',]
