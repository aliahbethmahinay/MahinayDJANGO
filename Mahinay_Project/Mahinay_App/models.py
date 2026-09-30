from django.db import models


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    room_type = models.CharField(max_length=100)
    check_in_date = models.CharField(max_length=100)
    check_out_date = models.CharField(max_length=100)
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.guest_name