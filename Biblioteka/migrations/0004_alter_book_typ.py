# Generated by Django 3.2 on 2021-05-10 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0003_alter_book_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='typ',
            field=models.CharField(choices=[('Miękka', 'Miękka'), ('Twarda', 'Twarda')], max_length=6),
        ),
    ]
