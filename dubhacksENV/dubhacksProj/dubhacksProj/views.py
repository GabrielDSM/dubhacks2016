from django.shortcuts import render

def women(request):
    return render(request, 'women.html', {'page_name': 'Women'})
 
def hcde(request):
    return render(request, 'major.html', {'page_name': 'HCDE'})

def info(request):
    return render(request, 'major.html', {'page_name': 'INFO'})

def cse(request):
    return render(request, 'major.html', {'page_name': 'CSE'})

def about(request):
    return render(request, 'major.html', {'page_name': 'About'})