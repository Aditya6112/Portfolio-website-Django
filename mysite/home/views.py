from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is a boy view created by Aditya.")
def paths(request):
    return HttpResponse("This is a path view created by Aditya.")
