from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from recipeapp.models import Author, mails
from random import choice


class Command(BaseCommand):
    help = 'Create fake authors database.'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            author = Author(
                firstname=lorem_ipsum.words(1, common=False).capitalize(),
                lastname=lorem_ipsum.words(1, common=False).capitalize(),
            )
            author.email = f'{author.firstname[:3]}{author.lastname[:4]}{choice(mails)}'
            author.save()
