from django.shortcuts import render

from django.db import connection

def women(request):
    return render(request, 'women.html', {'page_name': 'Women'})

def hcde(request):
    return render(request, 'major.html', {'page_name': 'Human Centered Design and Engineering'})

def info(request):
    return render(request, 'major.html', {'page_name': 'Informatics'})

def cse(request):
    return render(request, 'major.html', {'page_name': 'Computer Science and Engineering'})

def about(request):
    return render(request, 'major.html', {'page_name': 'About'})
