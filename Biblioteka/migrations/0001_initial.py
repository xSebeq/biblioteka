# Generated by Django 3.2 on 2021-05-08 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('tytul', models.TextField()),
                ('autor', models.TextField()),
                ('typ', models.CharField(choices=[('miekka', 'Miękka'), ('twarda', 'Twarda')], max_length=6)),
                ('wydawnictwo', models.TextField()),
                ('data_premiery', models.DateField()),
                ('data_publikacji', models.DateField(default=None)),
                ('liczba_stron', models.IntegerField()),
                ('zdjecie', models.ImageField(upload_to='')),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_undelete', 'Can undelete this object'),),
                'abstract': False,
            },
        ),
    ]
