from django.core.management.base import BaseCommand
from recipeapp.models import Category, categories


class Command(BaseCommand):
    help = 'Fill Category DB'

    def handle(self, *args, **kwargs):
        for category in categories:
            new_category = Category(name=category)
            new_category.save()
