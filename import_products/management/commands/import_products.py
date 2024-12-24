import csv
from django.core.management.base import BaseCommand
from inventory.models import Product


class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Product.objects.create(name=row['name'], sku=row['sku'], category=row['category'],
                                       mass=row['mass'], unit=row['unit'])
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
