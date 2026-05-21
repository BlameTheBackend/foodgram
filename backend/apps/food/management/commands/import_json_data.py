import json
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.food.models import Ingredient


class Command(BaseCommand):
    help = 'Импорт ингредиентов из json файла'

    def handle(self, *args, **kwargs):
        json_path = (settings.BASE_DIR
                     / 'data'
                     / 'ingredients.json'
                     )
        with open(json_path, encoding='utf-8') as file:
            ingredients = json.load(file)

        for ingredient in ingredients:
            Ingredient.objects.get_or_create(
                name=ingredient['name'],
                measurement_unit=ingredient['measurement_unit']
            )

        self.stdout.write(self.style.SUCCESS('Ингредиенты загружены'))
