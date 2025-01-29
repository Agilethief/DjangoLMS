from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# TODO: Implement the views for the front end.
def home(request):
    # In a real-world application, this could just redirect to the actual front end.
    return HttpResponse("<h1>Home page for front end</h1>")
