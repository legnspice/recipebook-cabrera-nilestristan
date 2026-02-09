from django.shortcuts import render
from django.http import HttpResponse
from .data import recipes_data

def recipes_list(request):
    return render(request, "ledger/recipes_list.html", { "recipes": recipes_data })

def recipe(request, index):
    if index < 1 or index > 2:
        return HttpResponse("Invalid Index: Inaccessible Page")

    return render(request, "ledger/recipe.html", { "recipe": recipes_data[index - 1] })

