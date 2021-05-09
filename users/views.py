from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POSt)
        if form.is_valid():
            form.save()
        return redirect("")
    else:
        form = UserCreationForm
    return render(response, "users/zarejestruj.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            return redirect("")
        else:
            form = AuthenticationForm()
        return render(request, 'users/zaloguj.html', {'form':form})