from django import forms
from .models import Reservation

class Reservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_name', 'contact_number', 'room_type', 'check_in_date', 'check_out_date', 'number_of_guests' ]

        widgets = {
            'guest name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact number': forms.NumberInput(attrs={'class': 'form-control'}),
            'room type': forms.Select(attrs={'class': 'form-control'}),
            'check in date': forms.NumberInput(attrs={'class': 'form-control'}),
            'check out date': forms.NumberInput(attrs={'class': 'form-control'}),
            'number of guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }


