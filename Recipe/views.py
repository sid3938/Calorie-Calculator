from django.shortcuts import render
# Create your views here.

def Recipe(request):
  return render(request, "Recipe.html")