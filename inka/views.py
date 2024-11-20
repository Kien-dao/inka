from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'Home.html')

def product(request):
    return render(request, 'Product.html') 
    
def document(request):
    return render(request, 'Document.html') 
    
def introduce(request):
    return render(request, 'Introduce.html')

def service(request):
    return render(request, 'Service.html') 
    
def contact(request):
    return render(request, 'Contact.html')     

def djangosetup(request):
    return render(request, 'djangosetup.html')  
    
def htmlwork(request):
    return render(request, 'htmlwork.html') 
    