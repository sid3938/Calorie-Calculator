from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def calorie_calculator(request):
    return render(request, 'calorie_calculator.html')

