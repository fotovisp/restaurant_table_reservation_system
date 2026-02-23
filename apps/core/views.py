from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware, is_naive

from apps.core.models import Client, Restaurant_Table


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

            tables = Restaurant_Table.objects.create(
                floor = request.POST['floor'],
                is_busy = True,
                reserved_time = date,
                client = client)
            print(tables)
            return redirect("/")

    return render(request, 'core/tables.html',
                      {"table_list" : Restaurant_Table.objects.all(),
                              "client_list" : Client.objects.all()})

