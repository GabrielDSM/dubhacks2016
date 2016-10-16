from django.shortcuts import render

def women(request):
    person = "Student"
    return render(request, 'templates/women.html', {'name': person})