import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental.settings')
django.setup()

from rentals.models import Car
from django.conf import settings

# Get the first car
car = Car.objects.filter(available=True).first()

if car:
    print(f"Car: {car.year} {car.make} {car.model}")
    print(f"Image field: {car.image}")
    print(f"Image name: {car.image.name if car.image else 'None'}")
    print(f"Image URL: {car.image.url if car.image else 'None'}")
    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"MEDIA_URL: {settings.MEDIA_URL}")
    
    if car.image:
        image_path = os.path.join(settings.MEDIA_ROOT, car.image.name)
        print(f"Expected file path: {image_path}")
        print(f"File exists: {os.path.exists(image_path)}")
else:
    print("No cars found")

