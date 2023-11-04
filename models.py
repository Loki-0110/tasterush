from django.db import models

from restaurant.models import Dish


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, blank=False)
    mobile_no = models.BigIntegerField(blank=False, unique=True)

    class Meta:
        managed = False
        db_table = "user_table"

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
    quantity = models.IntegerField(default=1)
    time_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=1)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} ({self.time_ordered})"

