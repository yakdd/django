from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, RecipeImage
from .forms import AddRecipeForm, EditRecipeForm, ImageForm
from random import choices
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def index(request):
    count = 5
    rand_recipes = choices(Recipe.objects.all(), k=count)
    context = {
        'title': f'{count} random recipes',
        'count': count,
        'recipes': rand_recipes,
    }
    return render(request, 'recipeapp/index.html', context)


def recipes(request):
    all_recipes = Recipe.objects.all()
    context = {
        'title': 'All recipes list',
        'length': len(all_recipes),
        'recipes': all_recipes,
    }
    return render(request, 'recipeapp/recipes.html', context)


def recipe(request, id):
    find_recipe = get_object_or_404(Recipe, pk=id)
    recipe_images = RecipeImage.objects.filter(recipe_id=find_recipe).all()
    steps = find_recipe.steps.split('.')
    context = {
        'title': f'{find_recipe} details',
        'images': recipe_images,
        'recipe': find_recipe,
        'steps': steps,
    }
    return render(request, 'recipeapp/recipe.html', context)


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
                name=data['name'],
                category=data['category'],
                description=data['description'],
                steps=data['steps'],
                author=data['author'],
                cooking_time=data['cooking_time'],
            )
            return redirect('recipe', new_recipe.id)
    else:
        form = AddRecipeForm()
    return render(request, 'recipeapp/add-recipe.html', {'form': form})


def edit_recipe(request, recipe_id):
    find_recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_images = RecipeImage.objects.filter(recipe_id=find_recipe).all()
    if request.method == 'POST':
        form = EditRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            find_recipe.name = data['name']
            find_recipe.category = data['category']
            find_recipe.description = data['description']
            find_recipe.steps = data['steps']
            find_recipe.cooking_time = data['cooking_time']
            return redirect('recipes')
    else:
        form = EditRecipeForm(initial={
            'name': find_recipe.name,
            'category': find_recipe.category,
            'description': find_recipe.description,
            'steps': find_recipe.steps,
            'cooking_time': find_recipe.cooking_time,
        })

    context = {
        'images': recipe_images,
        'recipe': find_recipe,
        'form': form,
    }

    return render(request, 'recipeapp/recipe-edit.html', context)


def upload_image(request, recipe_id):
    find_recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(new_image.name, new_image)
            RecipeImage.objects.create(
                recipe_id=find_recipe,
                image=new_image,
            )
            return redirect('recipe', recipe_id)
    else:
        form = ImageForm()

    context = {
        'recipe': find_recipe,
        'form': form,
    }
    return render(request, 'recipeapp/upload-image.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


class AboutUser(TemplateView):
    template_name = 'recipeapp/about-user.html'


class Registration(CreateView):
    form_class = UserCreationForm
    template_name = 'recipeapp/registration.html'
    success_url = reverse_lazy('about_user')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user=user)
        return response
