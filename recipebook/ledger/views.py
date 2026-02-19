from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    context_object_name = 'recipe'

