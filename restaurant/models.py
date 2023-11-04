from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    email = models.CharField(max_length=100, blank=False, default="klankipalle@hotmail.com")
    class Meta:

        db_table = "restaurant_table"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    price = models.IntegerField()
    image_url = models.CharField()

    # Add other fields as needed (e.g., price, ingredients, etc.)

    class Meta:
        managed = False
        db_table = "dish_table"

    def __str__(self):
        return self.name



