from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes_list'),
    path('recipe/<int:index>/', recipe, name='recipe'),
]
# This might be needed, depending on your Django version
app_name = "ledger"