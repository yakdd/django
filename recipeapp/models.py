from django.db import models

categories = ['soups', 'main courses', 'snacks', 'salads', 'dessert', 'conservation']
mails = ['@yandex.ru', '@mail.ru', '@gmail.com', '@hotmail.com', '@outlook.com']


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    steps = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cooking_time = models.TimeField()

    def __str__(self):
        return f'{self.name}'


class RecipeImage(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')
