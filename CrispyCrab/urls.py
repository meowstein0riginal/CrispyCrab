"""CrispyCrab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crispy_crab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),

    path('ingredients/list', views.IngredientsList.as_view(), name='ingredientslist'),
    path('ingredients/create', views.IngredientsCreate.as_view(), name='ingredientscreate'),

    path('menu_items/list', views.MenuItemsList.as_view(), name='menuitemslist'),

    path('menu_items_management/list', views.MenuItemsManagementList.as_view(), name='menuitemsmanagementlist'),
    path('menu_items_management/create', views.MenuItemsManagementCreate.as_view(), name='menuitemsmanagementcreate'),

    path('recipe_requirements/list', views.RecipeRequirementsList.as_view(), name='reciperequirementslist'),
    path('recipe_requirements/create', views.RecipeRequirementsCreate.as_view(), name='reciperequirementscreate'),

    path('purchases/list', views.PurchaseList.as_view(), name='purchaselist'),

    path('purchases/create', views.PurchaseCreate.as_view(), name='purchasecreate'),

    path('restock_list', views.RestockList.as_view(), name='restocklist'),



]
