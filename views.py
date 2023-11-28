from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request,"samuka_app/home.html")
def contato (request):
    return render(request,"samuka_app/contato.html")
def desenvolvimento (request):
    return render(request,"samuka_app/desenvolvimento.html")
def sobremim (request):
    return render(request,"samuka_app/sobremim.html")
    