from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import RecipeIngredient, Recipe, Ingredient


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(DetailView):
    model = Recipe 
    template_name = 'recipe_detail.html'


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipe' : recipes}
    return render(request,'ledger/recipe_list.html', ctx)
    
    
def recipe_detail(request, id):
    ctx = {"recipe", Recipe.objects.get(id=id)}
    return render(request, 'recipe_detail.html', ctx)






# Create your views here.
