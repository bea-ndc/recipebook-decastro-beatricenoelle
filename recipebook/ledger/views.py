from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Recipe


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    redirect_field_name = 'login.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = 'login'


# Create your views here.
