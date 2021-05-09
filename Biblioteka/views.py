from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Book
from datetime import datetime


class WszystkieOpublikowaneKsiazki(ListView):
    model = Book
    template_name = "Biblioteka/opublikowane.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(data_publikacji__lte=datetime.today())


class WszystkieKsiazkiUzytkownika(ListView):
    model = Book
    template_name = "Biblioteka/ksiazki_uzytkownika.html"
    context_object_name = "books"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Book.objects.filter(uzytkownik = user)


class DodajKsiazke(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['tytul', 'autor', 'typ', 'wydawnictwo', 'data_premiery', 'data_publikacji', 'liczba_stron', 'zdjecie']
    template_name = "Biblioteka/dodaj.html"

    def form_valid(self, form):
        form.instance.uzytkownik = self.request.user
        return super().form_valid(form)


class EdycjaKsiazki(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['tytul', 'autor', 'typ', 'wydawnictwo', 'data_premiery', 'data_publikacji', 'liczba_stron', 'zdjecie']
    template_name = "Biblioteka/edytuj.html"

    def form_valid(self, form):
        form.instance.uzytkownik = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.uzytkownik:
            return True
        return False

def publikuj(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.user == book.uzytkownik:
        book.data_publikacji = datetime.today()
        book.save()
    return HttpResponse(book)