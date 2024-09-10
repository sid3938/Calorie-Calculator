from django.shortcuts import render
from Counter.views import home
from Counter.models import FoodItem

# Create your views here.

def index(request):
  return render(request, "index.html")


def home(request):
  data = FoodItem.objects.all()
  return render(request, "home.html", {'data':data})

