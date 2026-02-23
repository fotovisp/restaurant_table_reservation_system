
from django.test import TestCase
from datetime import datetime
from django.utils import timezone

from apps.core.models import Client, Restaurant_Table


# Create your tests here.

class ClientModelTest(TestCase):
    def setUp(self):
            """Створення тестового клієнта перед кожним тестом"""
            self.client_data = {
            'client_surname': 'Smith',
            'client_firstname': 'John',
            'client_patronymic': 'Michaelson', # англомовний варіант по батькові
            'phone_number' : '+380(12)3456789'
            }
            self.client = Client.objects.create(**self.client_data)


    def test_create_client(self):
        """Перевірка всіх полів, щоб перевірити чи клієнт створюється правильно"""
        client = Client.objects.get(client_id=self.client.client_id)
        self.assertEqual(client.client_surname, self.client_data['client_surname'])
        self.assertEqual(client.client_firstname, self.client_data['client_firstname'])
        self.assertEqual(client.client_patronymic, self.client_data['client_patronymic'])
        self.assertEqual(client.phone_number, self.client_data['phone_number'])


    def test_read_client(self):
        """Перевірка, що дані клієнта можна коректно прочитати"""
        client = Client.objects.get(client_id=self.client.client_id)
        self.assertEqual(client.client_surname, 'Smith')
        self.assertEqual(client.client_firstname, 'John')
        self.assertEqual(client.phone_number, '+380(12)3456789')


    def test_update_client(self):
        """Перевірка, що клієнт оновлюється коректно"""
        self.client.client_surname = 'Johnson'
        self.client.client_firstname = 'James'
        self.client.save()
        updated_client = Client.objects.get(client_id=self.client.client_id)
        self.assertEqual(updated_client.client_surname, 'Johnson')
        self.assertEqual(updated_client.client_firstname, 'James')


    def test_delete_client(self):
        """Перевірка, що клієнт видаляється коректно"""
        temp_client_id = self.client.client_id
        self.client.delete()
        with self.assertRaises(Client.DoesNotExist):
            Client.objects.get(client_id=temp_client_id)



class Restaurant_Table_Test(TestCase):
    def setUp(self):
        self.client_data = {
            'client_surname': 'Smith',
            'client_firstname': 'John',
            'client_patronymic': 'Michaelson',  # англомовний варіант по батькові
            'phone_number': '+380(12)3456789'
        }
        self.client = Client.objects.create(**self.client_data)
        self.reserved_time = timezone.make_aware(datetime(2026,5,1, 14, 30, 0))
        self.table_data = {
            'floor' : 1,
            'is_busy' : True,
            'reserved_time' : self.reserved_time,
            'client' : self.client
        }
        self.table = Restaurant_Table.objects.create(**self.table_data)

    def test_create_table(self):
        table = Restaurant_Table.objects.get(id=self.table.id)
        self.assertEqual(table.floor, self.table_data['floor'])
        self.assertEqual(table.is_busy, self.table_data['is_busy'])
        self.assertEqual(table.reserved_time, self.table_data['reserved_time'])
        self.assertEqual(table.client, self.table_data['client'])

    def test_read_table(self):
        """Перевірка, що дані клієнта можна коректно прочитати"""
        table = Restaurant_Table.objects.get(id=self.table.id)
        self.assertEqual(table.floor, 1)
        self.assertEqual(table.is_busy, True)
        self.assertEqual(table.reserved_time, self.reserved_time)
        self.assertEqual(table.client, self.client)


    def test_update_table(self):
        """Перевірка, що клієнт оновлюється коректно"""
        self.table.floor = 2
        self.table.is_busy = False
        self.table.reserved_time = self.reserved_time
        self.table.client = self.client
        self.table.save()
        updated_table = Restaurant_Table.objects.get(id=self.table.id)
        self.assertEqual(updated_table.floor, 2)
        self.assertEqual(updated_table.is_busy, False)
        self.assertEqual(updated_table.reserved_time, timezone.make_aware(datetime(2026,5,1, 14, 30, 0)))
        self.assertEqual(updated_table.client, self.client)


    def test_delete_table(self):
        """Перевірка, що клієнт видаляється коректно"""
        temp_table_id = self.table.id
        self.table.delete()
        with self.assertRaises(Restaurant_Table.DoesNotExist):
            Restaurant_Table.objects.get(id=temp_table_id)