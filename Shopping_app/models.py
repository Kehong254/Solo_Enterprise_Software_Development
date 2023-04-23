from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()

    def __str__(self):
        return f'{self.customer_name} - {self.product.name}'

class Volcano(models.Model):
    ID = models.IntegerField(primary_key=True)
    Volcano_Name = models.CharField(max_length=100)
    Volcano_Image = models.URLField(max_length=100)
    Volcano_Type = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Region = models.CharField(max_length=100)
    Subregion = models.CharField(max_length=100)
    epoch_period = models.CharField(max_length=100)
    Summit_and_Elevation = models.CharField(max_length=100)
    Latitude = models.FloatField(max_length=100)
    Longitude = models.FloatField(max_length=100)

    def __str__(self):
        return self.Volcano_Name

