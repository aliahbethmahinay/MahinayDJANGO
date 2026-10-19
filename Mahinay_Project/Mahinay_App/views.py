
from django.shortcuts import render, redirect, get_object_or_404
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
        'form': form,
        'page_title': 'Add Reservation',
        'button_text': 'Save Reservation'
    })


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        reservation_id=reservation_id
    )

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)

        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'EasyStayApp/reservation_form.html', {
        'form': form,
        'page_title': 'Edit Reservation',
        'button_text': 'Update Reservation'
    })


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        reservation_id=reservation_id
    )

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')

    return render(request, 'EasyStayApp/reservation_confirm_delete.html', {
        'reservation': reservation
    })
