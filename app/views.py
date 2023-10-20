from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def test(request):
    return HttpResponse("<h1>Estas en Log In :)</h1>")  # Corregir esta línea