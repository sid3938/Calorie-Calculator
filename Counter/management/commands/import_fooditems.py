import json
from django.core.management.base import BaseCommand
from Counter.models import FoodItem
from decimal import Decimal, InvalidOperation

class Command(BaseCommand):
    help = 'Import food items from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            data = json.load(file)
            for row in data:
                try:
                    # Convert fields to Decimal where appropriate
                    FoodItem.objects.create(
                        name=row['name'],
                        serving_size=row['serving_size'],  # This is a CharField, so no conversion needed
                        calories=self.convert_to_decimal(row['calories']),
                        carbohydrate=self.convert_to_decimal(row['carbohydrate']),
                        cholesterol=self.convert_to_decimal(row['cholesterol']),
                        total_fat=self.convert_to_decimal(row['total_fat']),
                        saturated_fat=self.convert_to_decimal(row['saturated_fat']),
                        fiber=self.convert_to_decimal(row['fiber']),
                        protein=self.convert_to_decimal(row['protein']),
                        sodium=self.convert_to_decimal(row['sodium']),
                        sugars=self.convert_to_decimal(row['sugars'])
                    )
                except (InvalidOperation, KeyError, ValueError) as e:
                    self.stderr.write(f"Error importing item {row.get('name', 'Unknown')}: {e}")
        
        self.stdout.write(self.style.SUCCESS('Successfully imported data from JSON'))

    def convert_to_decimal(self, value):
        try:
            # Convert to Decimal, handling cases where value might be a string
            return Decimal(value)
        except (InvalidOperation, TypeError):
            # Handle conversion errors by returning a default value or raising an error
            return Decimal('0.00')
