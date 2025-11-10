from django.core.management.base import BaseCommand
from rentals.models import Car
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Updates the first car to use the 123.jpg image'

    def handle(self, *args, **options):
        # Get the first car (most recently created)
        car = Car.objects.filter(available=True).first()
        
        if not car:
            self.stdout.write(
                self.style.ERROR('No cars found in the database!')
            )
            return
        
        # Check if the image file exists
        image_path = os.path.join(settings.MEDIA_ROOT, 'cars', '123.jpg')
        
        if not os.path.exists(image_path):
            self.stdout.write(
                self.style.WARNING(f'Image file not found at: {image_path}')
            )
            self.stdout.write(
                self.style.WARNING('The file will be set in the database, but make sure 123.jpg is in the media/cars/ folder')
            )
            self.stdout.write(
                self.style.WARNING('Expected location: C:\\Users\\PC\\media\\cars\\123.jpg')
            )
        
        # Update the car's image field
        # We need to set it to the relative path that Django expects
        car.image.name = 'cars/123.jpg'
        car.save()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated {car.year} {car.make} {car.model} to use 123.jpg'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Car ID: {car.id}, Make: {car.make}, Model: {car.model}'
            )
        )

