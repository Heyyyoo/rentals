from django.core.management.base import BaseCommand
from rentals.models import Car
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Sets an image for a car by ID or make/model'

    def add_arguments(self, parser):
        parser.add_argument('image_filename', type=str, help='Image filename (e.g., car2.jpg)')
        parser.add_argument('--car-id', type=int, help='Car ID to update')
        parser.add_argument('--make', type=str, help='Car make (e.g., Toyota)')
        parser.add_argument('--model', type=str, help='Car model (e.g., Camry)')

    def handle(self, *args, **options):
        image_filename = options['image_filename']
        car_id = options.get('car_id')
        make = options.get('make')
        model = options.get('model')
        
        # Find the car
        if car_id:
            car = Car.objects.filter(id=car_id).first()
        elif make and model:
            car = Car.objects.filter(make=make, model=model).first()
        else:
            # Default to first car if no specific car is given
            car = Car.objects.filter(available=True).first()
        
        if not car:
            self.stdout.write(
                self.style.ERROR('No car found!')
            )
            return
        
        # Check if the image file exists
        image_path = os.path.join(settings.MEDIA_ROOT, 'cars', image_filename)
        
        if not os.path.exists(image_path):
            self.stdout.write(
                self.style.WARNING(f'Image file not found at: {image_path}')
            )
            self.stdout.write(
                self.style.WARNING(f'Please make sure {image_filename} is in the media/cars/ folder')
            )
            self.stdout.write(
                self.style.WARNING(f'Expected location: {image_path}')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Image file found at: {image_path}')
            )
        
        # Update the car's image field
        car.image.name = f'cars/{image_filename}'
        car.save()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated {car.year} {car.make} {car.model} (ID: {car.id}) to use {image_filename}'
            )
        )

