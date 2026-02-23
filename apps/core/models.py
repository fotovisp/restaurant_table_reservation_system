from django.db import models

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
    floor = models.IntegerField()
    is_busy = models.BooleanField()
    reserved_time = models.DateTimeField(null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}, {self.floor}, {self.is_busy}, {self.reserved_time}, {self.client}"
