from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.WszystkieOpublikowaneKsiazki.as_view()),
    path('opublikowane-uzytkownika/', views.WszystkieKsiazkiUzytkownika.as_view()),
    path('dodaj/', views.DodajKsiazke.as_view()),
    path('edytuj/<int:pk>', views.EdycjaKsiazki.as_view()),
    path('publikuj/<int:book_id>', views.publikuj),
    path('usun/<int:pk>', views.UsunKsiazke.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
