from django.db import models

# from product.models import Product
# from order.models import CustomerUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=1500)
    description = models.TextField()
    class Meta:
        db_table = "Categories"
        verbose_name_plural ="Categories"
    def __str__(self):
        return self.name
    
# class Variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, default='')
#     price = models.IntegerField(default= 0 )
#     sale_price = models.IntegerField(default=0)
#     inventory = models.IntegerField(default=0)
#     active = models.BooleanField(default= True)

# class Cart(models.Model):
#     user = models.ForeignKey(CustomerUser, on_delete= models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart , on_delete= models.CASCADE)
#     item = models.ForeignKey(Variation, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)

