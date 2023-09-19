from django.shortcuts import render, redirect

def home(request):
     return render(request, 'home.html')


def dashboard(request):
     return render(request, 'dashboard.html')

