from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from recipeapp.models import Author, Category, Recipe
from random import choice, randint


class Command(BaseCommand):
    help = 'Create fake recipes database.'

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        categories = Category.objects.all()

        for author in authors:
            for _ in range(randint(1, 3)):
                new_recipe = Recipe(
                    name=lorem_ipsum.words(1, common=False).capitalize(),
                    category=choice(categories),
                    description=lorem_ipsum.words(randint(10, 20), common=False).capitalize(),
                    steps='\n'.join(lorem_ipsum.paragraphs(randint(2, 10), common=False)),
                    author=author,
                    cooking_time=f'0{randint(0, 5)}:{randint(0, 5)}{choice((0, 5))}',
                )
                new_recipe.save()
                self.stdout.write(f'{author}.\n{new_recipe.category} - {new_recipe.name}.\n'
                                  f'{new_recipe.description}\n'
                                  f'{new_recipe.steps}\n'
                                  f'{new_recipe.cooking_time}')
