from django import forms
from .models import GoodsGroup, GoodsCreate

class GroupCreateFrom(forms.ModelForm):
    class Meta:
        model = GoodsGroup
        fields = ('name',)

class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = GoodsCreate
        fields = ('name', 'price', 'release_date', 'description', 'image', 'group')