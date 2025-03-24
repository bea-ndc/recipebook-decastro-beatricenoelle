from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    inlines = [RecipeIngredientInline,]


class RecipeImageAdmin(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageAdmin]


admin.site.register(Recipe, RecipeAdmin)


# Register your models here.
