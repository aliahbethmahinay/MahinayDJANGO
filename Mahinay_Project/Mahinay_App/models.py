from django.db import models


class Reservation(models.Model):

    reservation_id = models.AutoField(primary_key=True)

    guest_name = models.CharField(max_length=100)

    contact_number = models.CharField(max_length=20)

    room_type = models.CharField(max_length=100)

    check_in_date = models.DateField()

    check_out_date = models.DateField()

    number_of_guests = models.IntegerField()

    reservation_status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.guest_name