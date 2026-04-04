from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_surname = models.CharField(max_length=100, null=False)
    client_firstname = models.CharField(max_length=100, null=False)
    client_patronymic = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f"{self.client_id}, {self.client_surname}, {self.client_firstname}, {self.client_patronymic}, {self.phone_number}"

class Restaurant_Table(models.Model):
    id = models.AutoField(primary_key=True)
    floor = models.PositiveIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(3)])
    is_busy = models.BooleanField(default=False)
    reserved_time = models.DateTimeField(null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}, {self.floor}, {self.is_busy}, {self.reserved_time}, {self.client}"

class Booking(models.Model):
    table = models.ForeignKey(Restaurant_Table, on_delete=models.CASCADE, related_name='bookings')
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    booking_time = models.DateTimeField()
    duration_hours = models.PositiveIntegerField(default=2)

    def clean(self):
        if self.booking_time and self.booking_time < timezone.now():
            raise ValidationError("booking time cannot be in the past")

        duration = timezone.timedelta(hours=self.duration_hours)
        new_start = self.booking_time
        new_end = self.booking_time + duration

        overlap = Booking.objects.filter(
            Q(table=self.table)& #& означає 'and', це потрібно щоб запис відповідав всім вимогам одразу
            Q(booking_time__lt=new_end) &
            Q(booking_time__gt=new_start-duration)
        ).exclude(pk=self.pk) #виключення запису, щоб він не порівнював сам себе в базі даних

        if overlap.exists():
            raise ValidationError(f"table №{self.table.id} has been reserved before")

    def floor_info(self):
        return f"{self.table.floor} floor"

    def save(self, *args, **kwargs):
        self.full_clean() #повна перевірка перед тим, як дані потраплять у базу даних
        super().save(*args, **kwargs)