from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]
    

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
# Register your models here.
