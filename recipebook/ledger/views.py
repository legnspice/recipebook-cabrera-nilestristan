from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Profile, RecipeImage
from .forms import AddRecipeForm, UploadRecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = AddRecipeForm
    template_name = 'ledger/add_recipe_form.html'

    def form_valid(self, form):
        recipe = form.save(commit=False)
        profile = get_object_or_404(Profile, user=self.request.user)
        recipe.author = profile
        recipe.save()
        return super().form_valid(form)


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = UploadRecipeImageForm
    template_name = 'ledger/upload_image_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        recipe_image = form.save(commit=False)
        recipe_image.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        recipe_image.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.recipe.get_absolute_url()
