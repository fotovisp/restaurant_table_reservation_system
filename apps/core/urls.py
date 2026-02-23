from django.urls import path
from apps.core.views import about_project, client_table

urlpatterns = [
    path('about/', about_project),
    path('', client_table),
    ]