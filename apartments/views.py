from django.shortcuts import render

def index(request):
    return render(request, 'apartments/index.html')

def new(request):
    return render(request, 'apartments/index.html')

def interesting(request):
    return render(request, 'apartments/index.html')

def trash(request):
    return render(request, 'apartments/index.html')

def settings(request):
    return render(request, 'apartments/index.html')
