from django.shortcuts import render

# Create your views here.

def index(request):

    data = {}

    return render(request, 'pages/compoapp/index.html')

def fashion(request):
    
    data = {}

    return render(request, 'pages/compoapp/fashion.html')

def about(request):
    
    data = {}

    return render(request, 'pages/compoapp/about.html')

def travel(request):
    
    data = {}

    return render(request, 'pages/compoapp/travel.html')

def single(request):
    
    data = {}

    return render(request, 'pages/compoapp/single.html')

def contact(request):
    
    data = {}

    return render(request, 'pages/compoapp/contact.html')