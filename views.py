from django.shortcuts import render

# Create your views here.
def home (requests):
    return render(requests, "page_app/home.html"
    )
    
def footer (requests):
    return render(requests, "page_app/footer.html"
    )
    
def principal (requests):
    return render(requests, "page_app/principal.html"
    )
    
def header (requests):
    return render(requests, "page_app/header.html"
    )
    
