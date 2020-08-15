from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')
def index(request):
    return render(request, 'index.html')
def services(request):
    return render(request, 'services.html')



