from django import forms
from .models import Recipe, Author, Category


class AddRecipeForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select, label='Автор')
    name = forms.CharField(max_length=50, label='Название')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select, label='Категория')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    steps = forms.CharField(widget=forms.Textarea, label='Порядок приготовления')
    cooking_time = forms.TimeField(label='Время приготовления')


class EditRecipeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select, label='Категория')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    steps = forms.CharField(widget=forms.Textarea, label='Порядок приготовления')
    cooking_time = forms.TimeField(label='Время приготовления')


class ImageForm(forms.Form):
    image = forms.ImageField()


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название',
        }


class RegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=100, label='Имя')
    lastname = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
