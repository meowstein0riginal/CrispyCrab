from django import forms
from crispy_crab.models import Ingredients, MenuItems, RecipeRequirements, Purchase


class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class MenuItemsCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"


class MenuItemsCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = ("item_name", "item_description", "item_price")


class RecipeRequirementsCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
