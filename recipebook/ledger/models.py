from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(validators=[MinLengthValidator(255)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               related_name="authors", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'A recipe called {}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.id)])


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return 'An ingredient called {}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', kwargs={'pk': self.pk})


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return f"{self.recipe.name}: {self.quantity} of {self.ingredient.name}"
