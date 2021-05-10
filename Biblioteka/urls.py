from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Biblioteka'
urlpatterns = [
    path('', views.WszystkieOpublikowaneKsiazki.as_view(), name="home"),
    path('opublikowane-uzytkownika/', views.WszystkieKsiazkiUzytkownika.as_view(), name="opublikowane-uzytkownika"),
    path('dodaj/', views.DodajKsiazke.as_view(), name="dodaj"),
    path('edytuj/<int:pk>', views.EdycjaKsiazki.as_view(), name="edytuj"),
    path('publikuj/<int:book_id>', views.publikuj, name="publikuj"),
    path('usun/<int:pk>', views.UsunKsiazke.as_view(), name="usun"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
