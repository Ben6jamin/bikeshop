from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("<h1>Welcome to the Bike Shop API</h1><p>Use /api/ to access the API endpoints.</p>")
