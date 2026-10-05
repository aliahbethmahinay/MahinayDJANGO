from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation

        fields = [
            'guest_name',
            'contact_number',
            'room_type',
            'check_in_date',
            'check_out_date',
            'number_of_guests',
            'reservation_status',
        ]

        widgets = {
            'guest_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter guest name'
            }),

            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),

            'room_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room type'
            }),

            'check_in_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'check_out_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'number_of_guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter number of guests',
                'min': 1
            }),

            'reservation_status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }