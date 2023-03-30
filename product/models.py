from django.db import models

from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=1500)
    price = models.DecimalField(max_digits=6, decimal_places=6)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='photos/products' , null=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    view = models.IntegerField()

    class Meta:
        db_table = "Products"
        verbose_name_plural ="Products"
    def __str__(self):
        return self.name