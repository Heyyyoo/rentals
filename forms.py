from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import RentalRequest

class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = RentalRequest
        fields = ['customer_name', 'customer_email', 'customer_phone', 'start_date', 'end_date', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '09XXXXXXXXX', 'maxlength': '11', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any additional information...'}),
        }
        labels = {
            'customer_name': 'Full Name',
            'customer_email': 'Email Address',
            'customer_phone': 'Phone Number',
            'start_date': 'Rental Start Date',
            'end_date': 'Rental End Date',
            'message': 'Additional Message (Optional)',
        }
    
    def clean_customer_phone(self):
        phone = self.cleaned_data.get('customer_phone')
        
        if phone:
            # Remove any whitespace
            phone = phone.strip()
            
            # Check if phone contains only digits
            if not phone.isdigit():
                raise ValidationError('Phone number must contain only numbers.')
            
            # Check if phone has maximum 11 digits
            if len(phone) > 11:
                raise ValidationError('Phone number must not exceed 11 digits.')
            
            # Check if phone has at least 1 digit (minimum validation)
            if len(phone) < 1:
                raise ValidationError('Phone number is required.')
        
        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date < date.today():
                raise ValidationError({'start_date': 'Start date cannot be in the past.'})
            if end_date < start_date:
                raise ValidationError({'end_date': 'End date must be after start date.'})
        
        return cleaned_data

