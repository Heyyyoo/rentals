from django.core.management.base import BaseCommand
from rentals.models import Car

class Command(BaseCommand):
    help = 'Adds sample cars to the database'

    def handle(self, *args, **options):
        sample_cars = [
            {
                'make': 'Toyota',
                'model': 'Camry',
                'year': 2023,
                'color': 'Silver',
                'price_per_day': 45.00,
                'description': 'A reliable and comfortable sedan perfect for city driving and long trips. Features modern technology and excellent fuel economy.',
                'available': True,
            },
            {
                'make': 'Honda',
                'model': 'Civic',
                'year': 2024,
                'color': 'Blue',
                'price_per_day': 40.00,
                'description': 'Compact and efficient, the Honda Civic is ideal for daily commutes. Great fuel economy and modern features.',
                'available': True,
            },
            {
                'make': 'BMW',
                'model': '3 Series',
                'year': 2023,
                'color': 'Black',
                'price_per_day': 85.00,
                'description': 'Luxury sedan with premium features, powerful engine, and exceptional driving experience. Perfect for those who want style and performance.',
                'available': True,
            },
            {
                'make': 'Mercedes-Benz',
                'model': 'C-Class',
                'year': 2024,
                'color': 'White',
                'price_per_day': 90.00,
                'description': 'Elegant luxury sedan with cutting-edge technology, premium interior, and smooth ride. Experience the best in comfort and style.',
                'available': True,
            },
            {
                'make': 'Ford',
                'model': 'F-150',
                'year': 2023,
                'color': 'Red',
                'price_per_day': 75.00,
                'description': 'Powerful pickup truck perfect for hauling and towing. Spacious interior and rugged capability for any adventure.',
                'available': True,
            },
            {
                'make': 'Tesla',
                'model': 'Model 3',
                'year': 2024,
                'color': 'White',
                'price_per_day': 95.00,
                'description': 'Electric vehicle with cutting-edge technology, autopilot features, and zero emissions. Experience the future of driving.',
                'available': True,
            },
        ]

        for car_data in sample_cars:
            car, created = Car.objects.get_or_create(
                make=car_data['make'],
                model=car_data['model'],
                year=car_data['year'],
                defaults=car_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created car: {car.year} {car.make} {car.model}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Car already exists: {car.year} {car.make} {car.model}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully added {len(sample_cars)} sample cars!')
        )

