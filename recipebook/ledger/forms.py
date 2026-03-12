from django import forms

from .models import Recipe, RecipeImage


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]
        labels = {"name": "Recipe Name"}


class UploadRecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description"]
