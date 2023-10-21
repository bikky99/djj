from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'John', 'age': 23},
        {'name': 'Jack', 'age': 25},
        {'name': 'Jill', 'age': 27},
    ]
    return render (request, 'box/index.html', {'peoples': peoples, 'page_title': 'Home'})

def contact(request):
    context = {'page_title': 'Contact Us'}
    return render (request, 'box/contact.html', context)

def about(request):
    context = {'page_title': 'About Us'}
    return render (request, 'box/about.html', context)
