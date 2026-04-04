from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware, is_naive
from django.contrib import messages
from django.core.exceptions import ValidationError

from apps.core.models import Client, Restaurant_Table, Booking


# Create your views here.

def about_project(request):
    return render(request, 'about.html')

def client_table(request):
    if request.method == 'POST':
        form_type = request.POST['form_type']
        if form_type == 'client':
            r_client = Client.objects.create(
                client_surname=request.POST['client_surname'],
                client_firstname=request.POST['client_firstname'],
                client_patronymic=request.POST['client_patronymic'],
                phone_number=request.POST['phone_number']
            )
            print(r_client)
            return redirect("/") #перекид на /
        elif form_type == 'table':
            reserved_time = request.POST['reserved_time']
            date = parse_datetime(reserved_time)

            if date and is_naive(date): #перевірка чи дата не пуста і без часового поясу
                date = make_aware(date) #додаємо часовий пояс

            client_id = request.POST['client_id']
            client = None
            if client_id:
                try:
                    client = Client.objects.get(client_id=client_id)
                except Client.DoesNotExist:
                    client = None

            try:
                table, created = Restaurant_Table.objects.get_or_create(
                    floor=request.POST['floor'],
                    defaults={'is_busy': True}
                )

                new_booking = Booking(
                    table=table,
                    client=client,
                    booking_time=date
                )
                new_booking.full_clean()
                new_booking.save()

                table.is_busy = True
                table.reserved_time = date
                table.client = client
                table.save()

                messages.success(request, "Бронювання успішне!")
                return redirect("/")
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)

    return render(request, 'core/tables.html',
                      {"table_list" : Restaurant_Table.objects.all(),
                              "client_list" : Client.objects.all()})

