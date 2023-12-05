from django.shortcuts import render

# Create your views here.
def index (requests):
    return render(requests, "page_app/index.html")
    
def sobre_mim (requests):
    return render(requests, "page_app/sobre_mim.html")
    
def contato (requests):
    return render(requests, "page_app/contato.html")
    
def main (requests):
    return render(requests, "page_app/main.html" )

def header (requests):
    return render(requests, "page_app/header.html")
    
def footer (requests):
    return render(requests, "page_app/footer.html")

def home (requests):
    return render(requests, "page_app/home.html")