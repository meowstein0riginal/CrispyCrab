from django import forms
from crispy_crab.models import Ingredients, MenuItems, RecipeRequirements, Purchase


class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class MenuItemsCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"


class MenuItemsManagementUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"


class RecipeRequirementsCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"


class RecipeRequirementsUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
