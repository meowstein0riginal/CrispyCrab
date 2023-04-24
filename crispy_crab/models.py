from django.db import models
from math import ceil

class Ingredients(models.Model):
    PIECE = "PC"
    GRAM = "GR"
    MILLILITRE = "ML"

    INGREDIENT_UNIT_CHOICES = [
        (PIECE, "pcs."),
        (GRAM, "gr."),
        (MILLILITRE, "ml")
    ]

    ing_name = models.CharField(max_length=25, unique=True)
    ing_quantity = models.IntegerField(default=0)
    multi_pack_quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=2, choices=INGREDIENT_UNIT_CHOICES, default=PIECE)
    multi_pack_price = models.DecimalField(max_digits=8, decimal_places=2)
    minimal_quantity = models.IntegerField(default=0)


    class Meta:
        ordering = ['ing_name']

    def __str__(self):
        return "ingredient: " + str(self.ing_name)

    # Returns how many multipacks needs to be ordered to stock up above minimum
    def ordering_qty(self):
        shortage = self.minimal_quantity - self.ing_quantity
        multipacks = ceil(shortage / self.multi_pack_quantity)
        x = int(multipacks)
        return x



    # returns price per unit to allow calculation of menu items cost
    def price_per_unit(self):
        price = getattr(self, "multi_pack_price")
        quantity = getattr(self, "multi_pack_quantity")
        ppu = round(price/quantity, 3)
        return ppu

    def get_absolute_url(self):
        return "list"

class MenuItems(models.Model):
    item_name = models.CharField(max_length=30, unique=True)
    item_description = models.CharField(max_length=150, default="recipe requirements not complete")
    item_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)


    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return "Meal: " + str(self.item_name)

    def get_absolute_url(self):
        return "list"

    # returns cost of all ingredients
    def ingredient_cost(self):
        requirements = self.reciperequirements_set.all()
        price = 0
        for i in requirements:
            price += i.calc_price()
        return round(price, 2)

    def ingredients(self):
        return [i.ingredient.ing_name for i in self.reciperequirements_set.all()]

    # returns True if there is enough ingredients to make one meal
    def is_available(self):
        result = []
        for i in self.reciperequirements_set.all():
            if i.quantity <= i.ingredient.ing_quantity:
                result.append(True)
            else:
                result.append(False)
        return all(result)

    # returns how many meals can be made, based on ingredients cost
    def availability(self):
        enough_for = []
        for i in self.reciperequirements_set.all():
            enough_for.append(i.ingredient.ing_quantity/i.quantity)

        if len(enough_for) >= 1:
            return int(min(enough_for))

        else:
            return 0


class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.menu_item.item_name} | {self.ingredient.ing_name}: {self.quantity} {self.ingredient.unit}"

    class Meta:
        ordering = ['menu_item']

    def get_absolute_url(self):
        return "list"

    # returns cost of ingredient in exact quantity needed for the meal
    def calc_price(self):
        ppu = self.ingredient.price_per_unit()
        return ppu * self.quantity


class Purchase(models.Model):
    order_time = models.DateTimeField(auto_now_add=True)
    menu_items = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    table = models.IntegerField()

    def get_absolute_url(self):
        return "list"