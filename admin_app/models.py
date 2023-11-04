from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)

    class Meta:
        managed = False
        db_table = "admin_table"

    def __str__(self):
        return self.username


# class Restaurant(models.Model):
#     id = models.AutoField(primary_key=True)
#     restaurant_name = models.CharField(max_length=100, blank=False)
#     password = models.CharField(max_length=20, blank=False)
#     mobile_no = models.BigIntegerField(blank=False, unique=True)
#     state = models.CharField(max_length=25, blank=False)
#     district = models.CharField(max_length=50, blank=False)
#     pincode = models.IntegerField(blank=False)
#     address = models.CharField(max_length=200, blank=False)
#     pancard_no = models.CharField(max_length=10, blank=False, unique=True)
#     bank_name = models.CharField(max_length=50, blank=False)
#     bankaccount_no = models.CharField(max_length=16, blank=False)
#     IFSC_code = models.CharField(max_length=11, blank=False)
#     Gst_no = models.CharField(max_length=15, blank=False)
#
#     class Meta:
#         db_table = "restaurant_table"
#
#     def __str__(self):
#         return self.restaurant_name

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=20, blank=False, unique=True)
#     password = models.CharField(max_length=20, blank=False)
#     email = models.CharField(max_length=100, blank=False)
#     mobile_no = models.BigIntegerField(blank=False, unique=True)
#
#     class Meta:
#         db_table = "user_table"
#
#     def __str__(self):
#         return self.username


class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, blank=False)
    mobile_no = models.BigIntegerField(blank=False, unique=True)
    vehicle_no = models.CharField(blank=False, unique=True)
    pancard_no = models.CharField(max_length=10, blank=False, unique=True)
    banks = (("BOB", "BankOfBaroda"),("SBI", "StateBankOfIndia"),("HDFC","HDFC"),("AXIS","AXIS"))
    bank_name = models.CharField(max_length=50, blank=False, choices=banks)
    bankaccount_no = models.CharField(max_length=16, blank=False)
    IFSC_code = models.CharField(max_length=11, blank=False)

    class Meta:
        managed = False
        db_table = "partner_table"

    def __str__(self):
        return self.username


# class Restaurant(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     image_url = models.CharField()
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     class Meta:
#         db_table = "restaurant_table"
#
#     def __str__(self):
#         return self.name


# class Dish(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=False)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
#     price=models.IntegerField()
#     image_url = models.CharField()
#     # Add other fields as needed (e.g., price, ingredients, etc.)
#
#     class Meta:
#         db_table = "dish_table"
#     def __str__(self):
#         return self.name
#
#
# class Orders(models.Model):
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


