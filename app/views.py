from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
<<<<<<< HEAD
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def solicitud(request):
    return render(request, "solicitud.html")
=======
def Home(request):
    return HttpResponse("Hola mudno desde la app") 
def test(request):
    pass
>>>>>>> 290732422d6930192edd4a4859000fbe7fcd3b88
