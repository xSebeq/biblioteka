from django.urls import path
from . import views

urlpatterns = [
    path('opublikowane/', views.WszystkieOpublikowaneKsiazki.as_view()),
    path('opublikowane-uzytkownika/', views.WszystkieKsiazkiUzytkownika.as_view()),
    path('dodaj/', views.DodajKsiazke.as_view()),
    path('edytuj/<int:pk>', views.EdycjaKsiazki.as_view()),
]
