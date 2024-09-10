from django.contrib import admin
from .models import FoodItem

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
  list_display=("name",)

admin.site.register(FoodItem, FoodAdmin)