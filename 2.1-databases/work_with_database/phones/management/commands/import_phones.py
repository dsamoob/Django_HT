import csv
import os

print(os.getcwd())

from django.core.management.base import BaseCommand
from phones.models import Phone

# id;name;image;price;release_date;lte_exists
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:

            if phone['lte_exists'] == 'False':
                lte = 'no'
            else:
                lte = 'yes'

            item = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=lte,
                slug='-'.join(phone['name'].split())
            )
            item.save()
