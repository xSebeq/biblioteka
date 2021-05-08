from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Book
from datetime import datetime


class WszystkieOpublikowaneKsiazki(ListView):
    model = Book
    template_name = "Biblioteka/opublikowane.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(data_publikacji__lte=datetime.today())


class WszystkieKsiazkiUzytkownika(ListView, LoginRequiredMixin):
    model = Book
    template_name = "Biblioteka/ksiazki_uzytkownika.html"
    context_object_name = "books"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Book.objects.filter(uzytkownik = user)