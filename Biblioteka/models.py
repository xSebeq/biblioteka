from django.db import models
from softdelete.models import SoftDeleteObject
from django.contrib.auth.models import User


class Book(SoftDeleteObject):
    MIEKKA = "miekka"
    TWARDA = "twarda"
    TYPE_OF_BOOK_CHOICES = [
        (MIEKKA, "Miękka"),
        (TWARDA, "Twarda"),
    ]
    tytul = models.TextField()
    autor = models.TextField()
    typ = models.CharField(
        max_length=6,
        choices=TYPE_OF_BOOK_CHOICES,
    )
    wydawnictwo = models.TextField()
    data_premiery = models.DateField()
    data_publikacji = models.DateField(default=None, null=True, blank=True)
    liczba_stron = models.IntegerField()
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    zdjecie = models.ImageField()

    def __str__(self):
        return self.tytul
