from django.shortcuts import render

def women(request):
    person = "Student"
    return render(request, 'women.html', {'name': person})