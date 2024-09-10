from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    serving_size = models.CharField(max_length=50)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=5, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2)
    fiber = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    sodium = models.DecimalField(max_digits=5, decimal_places=2)
    sugars = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


    def get_calories(self):
        return self.calories
