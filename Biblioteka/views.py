from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from datetime import datetime


class WszystkieOpublikowaneKsiazki(ListView):
    model = Book
    template_name = "Biblioteka/opublikowane.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(data_publikacji__lte=datetime.today())