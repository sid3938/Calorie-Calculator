from django.shortcuts import render
from .models import FoodItem

def home(request):
    context = {}
    if request.method == "POST":
        query = request.POST.get('query')

        if query:

            food_items = FoodItem.objects.filter(name__icontains=query)

            if food_items.exists():
                context['food_items'] = food_items
            else:
                context['error_message'] = "No food items found for the given query."
        else:
            context['error_message'] = "Search query cannot be empty."

    return render(request, 'home.html', context)
