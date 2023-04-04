from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

from crispy_crab.models import Ingredients, MenuItems, RecipeRequirements, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from crispy_crab.forms import IngredientsCreateForm, MenuItemsCreateForm, RecipeRequirementsCreateForm
from crispy_crab.forms import IngredientsUpdateForm, MenuItemsManagementUpdateForm, RecipeRequirementsUpdateForm
from django.http import HttpResponse, HttpRequest

from django.core.exceptions import SuspiciousOperation

class HomeView(TemplateView):
  template_name = "crispy_crab/home.html"


class IngredientsList(ListView):
    model = Ingredients
    template_name = "crispy_crab/ingredients_list.html"


class IngredientsCreate(CreateView):
    model = Ingredients
    template_name = "crispy_crab/ingredients_create.html"
    form_class = IngredientsCreateForm


class IngredientsUpdate(UpdateView):
    model = Ingredients
    template_name = "crispy_crab/ingredients_update.html"
    form_class = IngredientsUpdateForm
    success_url = "/ingredients/list"


class IngredientsDelete(DeleteView):
    model = Ingredients
    template_name = "crispy_crab/ingredients_delete.html"
    success_url = "/ingredients/list"


class MenuItemsList(ListView):
    model = MenuItems
    template_name = "crispy_crab/menu_items_list.html"


class MenuItemsManagementList(ListView):
    model = MenuItems
    template_name = "crispy_crab/menu_items_management_list.html"


class MenuItemsManagementCreate(CreateView):
    model = MenuItems
    template_name = "crispy_crab/menu_items_management_create.html"
    form_class = MenuItemsCreateForm


class MenuItemsManagementUpdate(UpdateView):
    model = MenuItems
    template_name = "crispy_crab/menu_items_management_update.html"
    form_class = MenuItemsManagementUpdateForm
    success_url = "/menu_items_management/list"


class MenuItemsManagementDelete(DeleteView):
    model = MenuItems
    template_name = "crispy_crab/menu_items_management_delete.html"
    success_url = "/menu_items_management/list"


class RecipeRequirementsList(ListView):
    model = RecipeRequirements
    template_name = "crispy_crab/recipe_requirements_list.html"


class RecipeRequirementsCreate(CreateView):
    model = RecipeRequirements
    template_name = "crispy_crab/recipe_requirements_create.html"
    form_class = RecipeRequirementsCreateForm


class RecipeRequirementsUpdate(UpdateView):
    model = RecipeRequirements
    template_name = "crispy_crab/recipe_requirements_update.html"
    form_class = RecipeRequirementsUpdateForm
    success_url = "/recipe_requirements/list"


class RecipeRequirementsDelete(DeleteView):
    model = RecipeRequirements
    template_name = "crispy_crab/recipe_requirements_delete.html"
    success_url = "/menu_items_management/list"

class PurchaseList(ListView):
    model = Purchase
    template_name = "crispy_crab/purchase_list.html"


class PurchaseCreate(TemplateView):
    template_name = "crispy_crab/purchase_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [item for item in MenuItems.objects.all() if item.is_available()]
        return context

    #subtracts ingredients from ingredient list
    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItems.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirements_set

        purchase = Purchase(menu_items=menu_item)
        purchase.table = request.POST["table"]

        for req in requirements.all():
            ingredient = req.ingredient
            ingredient.ing_quantity -= req.quantity
            ingredient.save()

        purchase.save()

        return redirect("/purchases/list")


class RestockList(TemplateView):
    template_name = "crispy_crab/restock_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = [ingredient for ingredient in Ingredients.objects.all() if ingredient.ordering_qty() > 0]
        return context

