from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageUploadForm


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    redirect_field_name = 'login.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = 'login'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.object.pk})


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageUploadForm
    template_name = 'recipe_imageform.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        ctx['pk'] = pk
        ctx['form'] = RecipeImageUploadForm()
        return ctx

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        form = RecipeImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = RecipeImage()
            recipe_image.image = request.FILES.get('image')
            recipe_image.recipe = Recipe.objects.get(pk=pk)
            recipe_image.save()
            return redirect(reverse('ledger:recipe_detail', args=[pk]))
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


# Create your views here.
