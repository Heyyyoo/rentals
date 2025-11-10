from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Car, RentalRequest
from .forms import RentalRequestForm

def car_list(request):
    """Display all available cars"""
    cars = Car.objects.filter(available=True)
    return render(request, 'rentals/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    """Display car details and rental request form"""
    car = get_object_or_404(Car, id=car_id, available=True)
    
    if request.method == 'POST':
        form = RentalRequestForm(request.POST)
        if form.is_valid():
            rental_request = form.save(commit=False)
            rental_request.car = car
            rental_request.save()
            
            # Send email to admin
            subject = f'New Rental Request: {car.year} {car.make} {car.model}'
            message = f"""
New rental request received:

Car: {car.year} {car.make} {car.model}
Price per day: ${car.price_per_day}

Customer Information:
- Name: {rental_request.customer_name}
- Email: {rental_request.customer_email}
- Phone: {rental_request.customer_phone}
- Start Date: {rental_request.start_date}
- End Date: {rental_request.end_date}
- Total Days: {(rental_request.end_date - rental_request.start_date).days + 1}
- Total Cost: ${car.price_per_day * ((rental_request.end_date - rental_request.start_date).days + 1)}

Message:
{rental_request.message if rental_request.message else 'No additional message provided.'}

Please review this request in the admin panel.
"""
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@rentals.com',
                    ['june85933@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Your rental request has been submitted successfully! We will contact you soon.')
            except Exception as e:
                # Log the error for debugging (only in DEBUG mode)
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f'Email sending error: {str(e)}')
                messages.error(request, f'There was an error sending your request: {str(e)}. Please try again or contact us directly.')
            
            return redirect('car_detail', car_id=car.id)
    else:
        form = RentalRequestForm()
    
    return render(request, 'rentals/car_detail.html', {'car': car, 'form': form})
