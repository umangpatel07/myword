from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
     
    return render(request, "index.html")
    # return HttpResponse("Heyy, I'm Umang Patel Nice too meet you Python-django")

def city(request):
    return render(request, "city.html")
def usa(request):
    return render(request, "usa.html")
def uae(request):
    return render(request, "uae.html")
def gotham(request):
    return render(request, "gotham.html")
def london(request):
    return render(request, "london.html")
def canada(request):
    return render(request, "canada.html")
def NorthKorea(request):
    return render(request, "NorthKorea.html")