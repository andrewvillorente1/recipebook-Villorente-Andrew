from django.db import models
from django.urls import reverse

class Ingredient(models.Model): #has ingredient + quantity
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[self.pk])

class Recipe(models.Model): #has recipe 1 + recipe 2
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return reverse('ledger:recipe', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=60)
    ingredient = models.ForeignKey(
        'Ingredient', 
        on_delete=models.CASCADE, 
        related_name="recipe"
        )
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE, 
        related_name="ingredients"
        )
