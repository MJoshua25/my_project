from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/index.html")

def contact(request):
    return render(request, "pages/contact.html")

def categorie(request):
    return render(request, "pages/categorie.html")

def blog(request):
    return render(request, "pages/blog.html")

def regular(request):
    return render(request, "pages/regular.html")