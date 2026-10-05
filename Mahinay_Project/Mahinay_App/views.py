from django.shortcuts import render, redirect

from .models import Reservation
from .forms import ReservationForm


def reservation_list(request):
    reservations = Reservation.objects.all()

    return render(request, 'EasyStayApp/reservation_list.html', {
        'reservations': reservations
    })


def add_reservation(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reservation_list')

    else:
        form = ReservationForm()

    return render(request, 'EasyStayApp/reservation_form.html', {
        'form': form
    })